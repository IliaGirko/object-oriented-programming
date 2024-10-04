import pytest

from src.category import Category
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture()
def cat_1():
    return Category(
        "телефон",
        "смартфон",
        [
            {"name": "телефон", "description": "смартфон", "price": 12000.0, "quantity": 1},
            {"name": "TV", "description": "ЖК", "price": 120000.0, "quantity": 10},
        ],
    )


@pytest.fixture()
def cat_2():
    return Category("телевизор", "ЖК", [{"name": "TV", "description": "ЖК", "price": 120000.0, "quantity": 10}])


@pytest.fixture()
def cat_3():
    return Category("телевизор", "ЖК", [Product("TV", "QLED", 1200, 12)])


@pytest.fixture()
def smartphone_1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


def test_init(cat_1, cat_2):
    assert cat_1.name == "телефон"
    assert cat_2.name == "телевизор"

    assert cat_1.description == "смартфон"
    assert cat_2.description == "ЖК"


def test_count_category():
    assert Category.category_count == 2


def test_add_product(cat_1, smartphone_1):
    assert cat_1.product_count == 5
    cat_1.add_product(smartphone_1)
    assert cat_1.product_count == 6


def test_add_product_error(cat_1):
    with pytest.raises(TypeError):
        cat_1.add_product("test")


def test_str(cat_3):
    assert str(cat_3) == "телевизор, количество продуктов: 12 шт."
