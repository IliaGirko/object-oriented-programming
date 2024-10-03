import pytest

from src.category import Category
from src.product import Product


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


def test_init(cat_1, cat_2):
    assert cat_1.name == "телефон"
    assert cat_2.name == "телевизор"

    assert cat_1.description == "смартфон"
    assert cat_2.description == "ЖК"


def test_count_category():
    assert Category.category_count == 2


def test_count_product():
    assert Category.product_count == 3


def test_add_proguct(cat_1):
    assert Category.product_count == 5
    cat_1.add_product("test")
    assert Category.product_count == 6


def test_str(cat_3):
    assert str(cat_3) == "телевизор, количество продуктов: 12 шт."
