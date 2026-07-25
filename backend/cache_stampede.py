'''
Problem: if a popular key expires and many requests simultaneously query the database, 
you may need locking/request coalescing

Solution: A common solution is to use a distributed lock in Redis so only one request 
loads the missing value from the database while other requests wait and then read the 
newly cached value.
--------------------------------------------------------------------------------------
                 Cache HIT
                    │
Request ───────► Redis ─────────────► Return
                    │
                 Cache MISS
                    │
                    ▼
              Acquire Lock?
              /           \
            YES            NO
             │              │
             ▼              ▼
       Double-check     Wait briefly
          cache             │
             │              ▼
             ▼         Cache populated?
          DB query         │
             │         YES ──► Return
             ▼
        Set cache
             │
             ▼
           Return
--------------------------------------------------------------------------------------
                    Redis Cache
                   /           \
             Instance A     Instance B
                 │               │
           Single-flight     Single-flight
                 │               │
                 └──── Redis Lock ────┘
                         │
                         ▼
                       DB
--------------------------------------------------------------------------------------
Redis cache + Redis distributed lock + local request coalescing (if needed) + 
short TTL + negative caching for missing users + metrics/monitoring.
'''
import asyncio
import json

import redis.asyncio as redis


redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
)

CACHE_TTL = 300
LOCK_TIMEOUT = 10
WAIT_TIMEOUT = 5

async def get_user(user_id: int):
    '''get'''
    cache_key = f"user:{user_id}"
    lock_key = f"lock:{cache_key}"

    # 1. Fast path: cache hit
    cached = await redis_client.get(cache_key)

    if cached is not None:
        return json.loads(cached)

    # 2. Create a distributed lock
    lock = redis_client.lock(
        lock_key,
        timeout=LOCK_TIMEOUT,
        blocking=False,
    )

    # 3. Try to become the request responsible
    #    for loading the cache
    acquired = await lock.acquire()

    if acquired:
        try:
            # 4. Double-check cache.
            # Another request may have populated it
            # before we acquired the lock.
            cached = await redis_client.get(cache_key)

            if cached is not None:
                return json.loads(cached)

            # 5. Only the lock owner queries the database
            user = await database_get_user(user_id)

            if user is None:
                # Optionally cache "not found" to prevent
                # repeated DB queries for nonexistent users.
                await redis_client.set(
                    cache_key,
                    json.dumps(None),
                    ex=60,
                )
                return None

            # 6. Populate cache
            await redis_client.set(
                cache_key,
                json.dumps(user),
                ex=CACHE_TTL,
            )

            return user

        finally:
            # Safe lock release
            if await lock.owned():
                await lock.release()

    # 7. Another request owns the lock.
    # Wait for it to populate the cache.
    deadline = asyncio.get_running_loop().time() + WAIT_TIMEOUT

    while asyncio.get_running_loop().time() < deadline:
        await asyncio.sleep(0.1)

        cached = await redis_client.get(cache_key)

        if cached is not None:
            return json.loads(cached)

    # 8. Bounded fallback.
    # The lock owner may have failed or Redis may be unhealthy.
    # Don't wait forever.
    raise RuntimeError(
        f"Could not load user {user_id} from cache"
    )


def database_get_user(user_id):
    '''get'''
    return {user_id}
