import pytest

from src.product import Product


@pytest.fixture()
def pr_1():
    return Product("телефон", "смартфон", 12000.0, 1)


@pytest.fixture()
def pr_2():
    return Product("телевизор", "ЖК", 1000.0, 10)


@pytest.fixture()
def pr_3():
    return Product("телевизор", "ЖК", 1000.0, 0)


def test_init(pr_1, pr_2):
    assert pr_1.name == "телефон"
    assert pr_2.name == "телевизор"

    assert pr_1.description == "смартфон"
    assert pr_2.description == "ЖК"

    assert pr_1.price == 12000.0
    assert pr_2.price == 1000.0

    assert pr_1.quantity == 1
    assert pr_2.quantity == 10


def test_new_product():
    assert Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


def test_price(pr_1):
    pr_1.price = 0.0
    assert "Цена не должна быть нулевая или отрицательная"

    pr_1.price = 100000.0
    assert pr_1.price == 100000.0


def test_str(pr_1):
    assert str(pr_1) == "телефон, 12000.0 руб. Остаток: 1 шт."


def test_add(pr_1, pr_2):
    assert pr_1 + pr_2 == 22000.0


def test_add_error(pr_1):
    with pytest.raises(TypeError):
        pr_1 + 1


def test_quantity_zero():
    try:
        Product("телевизор", "ЖК", 1000.0, 0)
    except ValueError:
        assert "Товар с нулевым количеством не может быть добавлен"
