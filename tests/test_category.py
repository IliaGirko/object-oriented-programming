import pytest

from src.category import Category


@pytest.fixture()
def cat_1():
    return Category("телефон", "смартфон", ["apple", "samsung"])


@pytest.fixture()
def cat_2():
    return Category("телевизор", "ЖК", ["sony"])


def test_init(cat_1, cat_2):
    assert cat_1.name == "телефон"
    assert cat_2.name == "телевизор"

    assert cat_1.description == "смартфон"
    assert cat_2.description == "ЖК"

    assert cat_1.products == ["apple", "samsung"]
    assert cat_2.products == ["sony"]


def test_count_category():
    assert Category.category_count == 2


def test_count_product():
    assert Category.product_count == 3
