from abc import ABC, abstractmethod

class Chair(ABC):

    @abstractmethod
    def chair_function(self):
        pass