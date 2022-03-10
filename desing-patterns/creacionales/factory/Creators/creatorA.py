from Interfaces.Creator import Creator
from Products.ProductA import ProductA


class ConcreteCreatorA(Creator):
    def factory_method(self) -> ProductA:
        return ProductA()


