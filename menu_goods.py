import aiosqlite

from typing import NamedTuple


class GoodsType(NamedTuple):
    db_id: int
    readable_name: str
    price: int


async def get_all_goods() -> tuple[GoodsType, ...]:
    async with aiosqlite.connect("actual_db.db") as aiosqlite_db:
        cur = await aiosqlite_db.execute("SELECT (id, readable_name, price) from goods")
        goods = cur.fetchall()
    return goods


async def get_single(db_id: int) -> GoodsType:
    async with aiosqlite.connect("actual_db.db") as aiosqlite_db:
        cur = await aiosqlite_db.execute("SELECT (id, readable_name, price) from goods WHERE id = (?)", db_id)
        single_id = cur.fetchone()
    return single_id
