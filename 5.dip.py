"""
Dependency Inversion Principle

Dependências devem ser feitas sobre abstrações, não sobre implementações concretas 

"""
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self,name,hp,speed):
        self.__name = name
        self.__hp = hp
        self.__speed = speed
    
    @abstractmethod
    def hp(self):
        pass

    @abstractmethod
    def name(self):
        pass

class Player(Entity):
    def __init__(self, name):
        self.stats = StatsReporter(self)
        self.__name = name
        self.__hp = 100
        self.__speed = 1

    def hp(self):
        return self.__hp

    def name(self):
        return self.__name

class StatsReporter:
    def __init__(self, char: Entity):
        self.char = char

    def report(self):
        print(f'Name:{self.char.name()}')
        print(f'HP:{self.char.hp()}')
