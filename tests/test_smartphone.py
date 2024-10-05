import pytest

from src.smartphone import Smartphone


@pytest.fixture
def phone_1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def phone_2():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


def test_add(phone_1, phone_2):
    assert phone_1 + phone_2 == 360000.0


def test_add_error(phone_1):
    with pytest.raises(TypeError):
        phone_1 + 1
