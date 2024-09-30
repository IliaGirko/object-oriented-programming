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
