from .redis import get_connection_async_redis


async def clear_cache(pattern: str) -> None:
    """Clear cache whose key matches the pattern"""

    conn = get_connection_async_redis()
    for k in await conn.keys():
        if pattern in k:
            await conn.delete(k)
    await conn.close()
