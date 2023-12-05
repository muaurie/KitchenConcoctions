import random
from animal import Animal
from ingredients import get_random_ing, cook_ingredients
class Dog(Animal):
    def __init__(self):
        dog_name = input("What is your dog's name? ")
        super().__init__(dog_name, 100)
        self.dog_name = dog_name
    def do_a_trick(self):
        print(f"{self.dog_name} does a backflip!")
    def do_an_oopsie(self):
        print(f"{self.dog_name} poops on the carpet!")
    def do_a_puppy_eyes(self):
        print(f"{self.dog_name} makes a sorrowful, and longing expression..")
    def check_win(self):
        if self.energy >= 200:
            print("Contgratulations! You've reached your target energy level!")
            return True
        return False


   