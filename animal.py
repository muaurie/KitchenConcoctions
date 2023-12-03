import random
class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    def eat(self, function_code, x):
        if function_code == "Eat":
            self.energy += x
            print(f"{self.name} eats the kitchen concoction and gains {x} energy!")
        elif function_code == "Eat 1/2":
            self.energy += x/2
            print(f"{self.name} eats half of the kitchen concoction and gains {x/2} energy!")

    ##get random expended energy
    def calc_expent_energy(self):
        energy_expent = random.randint(1,75)
        self.energy -= energy_expent
        return self.energy 

    ## if expended energy is below 50, follow function code instructions
    '''def energy_low(self):
        if self.energy < 50:
            if self.energy >= 30:
                self.eat("Eat 1/2", 10) ## ex 10 = energy gained from 1/2 treat'''

   
        