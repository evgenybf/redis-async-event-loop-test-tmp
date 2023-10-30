import logging
from unittest import IsolatedAsyncioTestCase, main

from .cache import clear_cache
from .redis import pool


class TestPublicHolidaysDataRetrieval(IsolatedAsyncioTestCase):

    async def asyncSetUp(self) -> None:
        await clear_cache("key")

    async def asyncTearDown(self) -> None:
        await pool.disconnect()
        pool.reset()

    async def test_func_1(self) -> None:
        ...

    async def test_func_2(self) -> None:
        ...


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(name)s %(levelname)s %(message)s')
    main()
