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

    def add_product(self, new_products):
        self.__products.append(new_products)
        Category.product_count += 1

    @property
    def products(self):
        product_string = ""
        for product in self.__products:
            product_string += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_string
