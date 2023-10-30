import logging

import redis.asyncio as aioredis

logger = logging.getLogger(__name__)

pool = aioredis.ConnectionPool(
    host="redis",
    port=6379,
)


def get_connection_async_redis():
    """get a new connection instance for redis (for async framework)"""
    logger.info("Open connection")
    try:
        return aioredis.Redis(
            connection_pool=pool,
            auto_close_connection_pool=False
        )
    except IOError:
        logger.exception("Error when connecting to redis...")
