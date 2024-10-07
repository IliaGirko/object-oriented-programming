from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            result = self.__price * self.quantity + other.__price * other.quantity
            return result
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_product_dict: dict):
        return cls(**new_product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price > 0:
            if new_price < self.__price:
                consent_verification_user = input(
                    "Введите y(значит yes) или n(значит no) для согласия понизить цену или для отмены действия: "
                )
                if consent_verification_user == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


# pr_1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#
# print(pr_1 + pr_1)
