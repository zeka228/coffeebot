from typing import NamedTuple


class GoodsType(NamedTuple):
    db_id: int
    readable_name: str
    price: int


async def get_all_goods() -> tuple[GoodsType, ...]:
    ...


async def get_single(db_id: int) -> GoodsType:
    ...
