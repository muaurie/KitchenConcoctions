class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
    def eat(self, function_code, x):
        if function_code == "Eat":
            print(f"{self.name} eats the kitchen concoction and gains {x} energy!")
        elif function_code == "Eat 1/2":
            print(f"{self.name} eats half of the kitchen concoction and gains {x/2} energy!")
        
   
        