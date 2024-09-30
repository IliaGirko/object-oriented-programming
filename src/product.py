class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.description = description
        self.price = price
        self.quantity = quantity
        self.name = name


pr1 = Product("телефон", "смартфон", 12000.0, 1)

print(pr1.name)
print(pr1.description)
print(pr1.price)
print(pr1.quantity)
