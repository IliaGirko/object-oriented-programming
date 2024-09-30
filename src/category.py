from typing import Any


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Any]):
        self.description = description
        self.products = products if products else []
        self.name = name
        Category.category_count += 1
        Category.product_count += len(products)
