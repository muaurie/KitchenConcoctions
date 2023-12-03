from animal import Animal
import random

class Human(Animal):
    def __init__(self):
        super().__init__(input("What is your name? "), 100)
    ##get random expended energy
    def calc_expend_energy(self):
        energy_expent = random.randint(1,75)
        self.energy -= energy_expent
        return self.energy
    ## if expended energy is below 50, follow function code instructions
    def energy_low(self):
        if self.energy < 50:
            if self.energy >= 30:
                self.eat("Eat 1/2", 10) ## ex 10 = energy gained from 1/2 treat

    def check_win(self):
        if self.energy_level >= 200:
            print("Contgratulations! You've reached your target energy level!")
            return True
        return False
    def check_lose(self):
        if self.energy_level < 25:
            print("Oops! Your energy level is too low. You're too hungry to go continue cooking for your pet!")
            return True
        return False

