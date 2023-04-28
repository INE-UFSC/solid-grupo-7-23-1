"""
Open-Closed Principle

Classes devem estar fechadas para modificação, mas abertas para extensão
"""
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        print(self.sound)

animals = [
    Animal('lion', 'roar'),
    Animal('mouse', 'squeak')
]

def animal_sound(animals: list):
    for animal in animals:
        animal.make_sound()

animal_sound(animals)


"""
Outro exemplo:

Imagine que você tem uma loja que dá desconto de 20% aos seus clientes favoritos
usando essa classe abaixo. Quando você decide dar 40% de desconto a clientes VIP,
você decide mudar a classe da seguinte forma:
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        return self.price * self.customer.discound

