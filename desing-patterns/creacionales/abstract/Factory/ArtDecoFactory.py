from Interfaces.FurnitureFactory import FurnitureFactory
from Furnitures.ArtDeco.ArtDecoChair import ArtDecoChair
from Furnitures.ArtDeco.ArtDecoCoffeeTable import ArtDecoCoffeeTable
from Furnitures.ArtDeco.ArtDecoSofa import ArtDecoSofa

class ArtDecoFactory(FurnitureFactory):

    def create_chair(self):
        return ArtDecoChair()


    def create_sofa(self):
        return ArtDecoSofa()

    def create_coffee_table(self):
        return ArtDecoCoffeeTable()
