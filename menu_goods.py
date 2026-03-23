import aiosqlite

from typing import NamedTuple


class GoodsType(NamedTuple):
    db_id: int
    readable_name: str
    price: int


async def get_all_goods() -> tuple[GoodsType, ...]:
    goods = []
    async with aiosqlite.connect("actual_db.db") as aiosqlite_db:
        fetch = await (await aiosqlite_db.execute(
            "SELECT id, readable_name, price "
            "from goods"
        )).fetchall()
        for _ in fetch:
            goods.append(GoodsType(*_))
    return tuple(goods)


async def get_single(db_id: int) -> GoodsType:
    async with aiosqlite.connect("actual_db.db") as aiosqlite_db:
        fetch = await (await aiosqlite_db.execute(
            "SELECT id, readable_name, price "
            "from goods "
            "WHERE id = (?)", (db_id,)
        )).fetchone()
    return GoodsType(*fetch)
