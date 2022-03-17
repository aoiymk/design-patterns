from Interfaces.FurnitureFactory import FurnitureFactory

from Factory.VictorianFactory import VictorianFactory
from Factory.ArtDecoFactory import ArtDecoFactory
from Factory.ModernFactory import ModernFactory

def client_code(factory: FurnitureFactory) -> None:

    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffeeTable = factory.create_coffee_table()

    print(f'Chair: {chair.chair_function()}')
    print(f'Sofa: {sofa.sofa_function()}')
    print(f'Coffee Table: {coffeeTable.coffee_table_function()}')


if __name__ == "__main__":

    print("Client: Testing client code with Victorian Factory")
    client_code(VictorianFactory())

    print('\n')

    print("Client: Testing client code with Modern Factory")
    client_code(ModernFactory())

    print('\n')
    print("Client: Testing client code with ArtDeco Factory")
    client_code(ArtDecoFactory())
