import imp
from Interfaces.Product import Product

class ProductA(Product):
    def operation(self) -> str:
        return "Soy el resultado el Producto A"
