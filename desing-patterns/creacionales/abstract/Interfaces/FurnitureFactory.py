from abc import ABC, abstractmethod
from curses.ascii import SO
from Interfaces.Chair import Chair
from Interfaces.CoffeeTable import CoffeeTable
from Interfaces.Sofa import Sofa

class FurnitureFactory(ABC):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass
