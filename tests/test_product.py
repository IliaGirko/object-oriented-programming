import pytest

from src.product import Product


@pytest.fixture()
def pr_1():
    return Product("телефон", "смартфон", 12000.0, 1)


@pytest.fixture()
def pr_2():
    return Product("телевизор", "ЖК", 1000.0, 10)


def test_init(pr_1, pr_2):
    assert pr_1.name == "телефон"
    assert pr_2.name == "телевизор"

    assert pr_1.description == "смартфон"
    assert pr_2.description == "ЖК"

    assert pr_1.price == 12000.0
    assert pr_2.price == 1000.0

    assert pr_1.quantity == 1
    assert pr_2.quantity == 10
