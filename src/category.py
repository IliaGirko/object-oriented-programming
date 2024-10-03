from typing import Any


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Any]):
        self.description = description
        self.__products = products if products else []
        self.name = name
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        result = 0
        for i in self.__products:
            result += i.quantity
        return f"{self.name}, количество продуктов: {result} шт."

    def add_product(self, new_products):
        self.__products.append(new_products)
        Category.product_count += 1

    @property
    def products(self):
        product_string = ""
        for product in self.__products:
            product_string += f"{str(product)}\n"
        return product_string
