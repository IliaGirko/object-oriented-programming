from src.lawn_grass import LawnGrass
from src.product import Product


def test_base_product(capsys):
    Product("телефон", "смартфон", 12000.0, 1)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(телефон, смартфон, 12000.0, 1)"

    LawnGrass("Газон", "трава", 12000.0, 1, "Russia", "5 дней", "Blue")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Газон, трава, 12000.0, 1)"
