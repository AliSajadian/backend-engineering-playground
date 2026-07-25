'''
Top 5 Users in Last 30 Days:
----------------------------------------------------------------------------

users
-----
id
name

orders
------
id
user_id
amount
created_at
----------------------------------------------------------------------------

SELECT
    u.id AS user_id,
    u.name,
    SUM(o.amount) AS total_amount
FROM users u
JOIN orders o
    ON u.id = o.user_id
WHERE o.created_at >= NOW() - INTERVAL '30 days'
GROUP BY
    u.id,
    u.name
ORDER BY
    total_amount DESC
LIMIT 5;
----------------------------------------------------------------------------

from datetime import datetime, timedelta, timezone

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

async def get_top_5_users(db: AsyncSession):
    since = datetime.now(timezone.utc) - timedelta(days=30)

    stmt = (
        select(
            User.id,
            User.username,
            func.count(Activity.id).label("activity_count"),
        )
        .join(Activity, Activity.user_id == User.id)
        .where(Activity.created_at >= since)
        .group_by(User.id, User.username)
        .order_by(func.count(Activity.id).desc())
        .limit(5)
    )

    result = await db.execute(stmt)
    return result.all()
----------------------------------------------------------------------------
'''
