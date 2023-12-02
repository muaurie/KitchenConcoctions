import random
from adoptioncenter import adoptable_dogs
class PocketDog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.happiness = 100
        self.hunger = 50

#Print list of available dogs to adopt 
    def adopt_pocketdogs(self, name, breed):
        adoption = input("Which dog would you like?")
        for PocketDog in self.adoptable_dogs:
            print(PocketDog.name, PocketDog.breed)
            adopted_dog = input("Enter the name of the dog you would like?")
            if adopted_dog in adoptable_dogs:
                self.adoptable_dogs.remove(PocketDog)
            else:
                print("That dog is not available for adoption")
            return adopted_dog