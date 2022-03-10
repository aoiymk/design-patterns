from Interfaces import Creator 

from Creators.creatorB import ConcreteCreatorB
from Creators.creatorA import ConcreteCreatorA


def client_code(creator: Creator) -> None:
    print(f"Client: Soy un cliente que debo ejecutar operaciones en multiples productos\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Probando ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")


    print("App: Probando ConcreteCreatorB.")
    client_code(ConcreteCreatorB())
    print("\n")
