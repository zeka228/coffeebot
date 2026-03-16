from enum import Enum


class Goods(Enum):
    espresso = 0
    americano = 1
    cappuccino = 2
    latte = 3
    raf = 4
    new_york = 5
    tiramisu = 6
    potato = 7
    brownie = 8
    strudel = 9


goods_data = {
    Goods.espresso: ["Эспрессо", 150],
    Goods.americano: ["Американо", 180],
    Goods.cappuccino: ["Капучино", 200],
    Goods.latte: ["Латте", 210],
    Goods.raf: ["Раф", 250],
    Goods.new_york: ["Чизкейк Нью-Йорк", 200],
    Goods.tiramisu: ["Тирамису", 200],
    Goods.potato: ["Пирожное Картошка", 90],
    Goods.brownie: ["Брауни", 250],
    Goods.strudel: ["Штрудель", 220]
}
