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


# ct1 = Category("телефон", "смартфон", ["apple","samsung"])
# ct2 = Category("телевизор", "ЖК", ["sony"])
#
# print(ct1.name)
# print(ct1.description)
# print(ct1.products)
# print(ct1.count_category)
# print(ct1.count_product)
# print(ct2.count_category)
# print(ct2.count_product)
#
#
# print(Category.count_category)
# print(Category.count_product)
