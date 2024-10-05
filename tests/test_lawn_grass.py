import pytest

from src.lawn_grass import LawnGrass


@pytest.fixture
def grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def grass_2():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


def test_add(grass_1, grass_2):
    assert grass_1 + grass_2 == 1000.0


def test_add_error(grass_1):
    with pytest.raises(TypeError):
        grass_1 + 1
