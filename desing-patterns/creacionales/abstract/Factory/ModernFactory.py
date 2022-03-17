from Interfaces.FurnitureFactory import FurnitureFactory
from Furnitures.Modern.ModernChair import ModernChair
from Furnitures.Modern.ModernCoffeeTable import ModernCoffeeTable
from Furnitures.Modern.ModernSofa import ModernSofa

class ModernFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()


    def create_sofa(self):
        return ModernSofa()

    def create_coffee_table(self):
        return ModernCoffeeTable()
