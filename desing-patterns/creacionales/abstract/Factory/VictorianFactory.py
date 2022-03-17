from Interfaces.FurnitureFactory import FurnitureFactory
from Furnitures.Victorian.VictorianChair import VictorianChair
from Furnitures.Victorian.VictorianCoffeeTable import VictorianCoffeeTable
from Furnitures.Victorian.VictorianSofa import VictorianSofa

class VictorianFactory(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()


    def create_sofa(self):
        return VictorianSofa()

    def create_coffee_table(self):
        return VictorianCoffeeTable()
