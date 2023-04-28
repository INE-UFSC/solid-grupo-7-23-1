"""
Liskov Substitution Principle

Uma subclasse deve ser substituível pela sua superclasse 
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        return self.name

class AnimalWithLegs(Animal):
    def leg_count(self) -> int:
        return 0

class AnimalLegless(Animal):
    def legs(self):
        print('I have no legs, dummy')

class Lion(AnimalWithLegs):
    def __init__(self):
        super().__init__('lion')

    def leg_count(self):
        return 4

class Snake(AnimalLegless):
    def __init__(self):
        super().__init__('snake')


def animal_leg_count(animals: list[AnimalWithLegs]):
    count = 0
    for animal in animals:
        count += animal.leg_count()
    return count
