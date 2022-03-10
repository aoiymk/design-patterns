from Interfaces.Product import Product

class ProductB(Product):
    def operation(self) -> str:
        return "Soy el resultado del producto B"