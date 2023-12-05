from animal import Animal
import random

class Human(Animal):
    def __init__(self):
        super().__init__(input("What is your name? "), 100)

    def check_lose(self):
        if self.energy < 25:
            print("Oops! Your energy level is too low. You're too hungry to go continue cooking for your pet!")
            return True
        return False

