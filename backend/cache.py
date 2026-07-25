'''
Caching

Request
   │
   ▼
Check Cache
   │
   ├── HIT ──────► Return cached user
   │
   └── MISS
         │
         ▼
    Query Database
         │
         ▼
    Store in Cache
         │
         ▼
    Return User
'''
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

    cached_user = await redis_client.get(cache_key)

    if cached_user is not None:
        return cached_user

    user = database_get_user(user_id)

    if user is None:
        return None

    redis_client.set(
        cache_key,
        user,
        ttl=300  # 5 minutes
    )

    return user


def update_user(user_id, data):
    '''update'''
    user = database_update_user(user_id, data)
    redis_client.delete(f"user:{user_id}")

    return user


def delete_user(user_id):
    '''delete'''
    database_delete_user(user_id)
    redis_client.delete(f"user:{user_id}")


def database_get_user(user_id):
    '''get'''
    return {user_id}


def database_update_user(user_id, data):
    '''get'''
    return {user_id, data}


def database_delete_user(user_id):
    '''get'''
    return {user_id}
