from Interfaces.Creator import Creator
from Products.ProductB import ProductB


class ConcreteCreatorB(Creator):
    def factory_method(self) -> ProductB:
        return ProductB()
