import random
from ingredients import get_random_ing, cook_ingredients
from animal import Animal
from dog import Dog
from human import Human

import random
##
def start_game():
    welcome = input(f"Welcome to Kitchen Concoctions. Would you like to hear the rules of the game? Y/N ")
    if welcome.upper() == "Y":
        print("In this game, you will attempt to cook treats for your dog so it will have energy to take a walk!")
        print("Both of you will start with 100 energy!")
        print("Your goal is for your pet's energy to reach level 200.")
        print("The void will give you 3 ingredients at random, it's your job to cook them and aim for most nutritional value to feed your pet!")
        print("Occassionally, you will get hungry (from all your hard work) and eat 1/2 of your pets treats.")
        print("If your energy reaches below 25, you lose the game!")
        input("Good luck! Press enter to start!")
    elif welcome.upper() == "N":
        input("Good luck! Press enter to start!")
  
    #instance of dog    
def indentify(owner, pet_dog):
    owner = Human()
    pet_dog = Dog()
    return owner, pet_dog

def get_nutritional_value():
     ##save get_random_ing() in random_ingredients
    random_ingredients = get_random_ing()
    #function for getting total
    total_nutritional_value = cook_ingredients(random_ingredients)
    return(total_nutritional_value, random_ingredients)

def mix_ingredients(owner, pet_dog, total_nutritional_value, ingredients_list):
    #calculate energy expent
    energy_expent = random.randint(1,85)
    #subtract this from owner's energy
    owner.energy -= energy_expent
    #if owner's energy is below 50, eat 1/2 of the treat
    if owner.energy <= 50:
        owner.eat("Eat 1/2", total_nutritional_value/2)
        #pet eat's 1/2 of treat also
        pet_dog.eat("Eat 1/2", total_nutritional_value/2)
    else:
        #otherwise pet will eat entire treat
        pet_dog.eat("Eat", total_nutritional_value)
    
    for ingredient in ingredients_list:
        print(f"{ingredient.name}: {ingredient.nutritional_value}")

    print(f"Total Nutritional Value: {total_nutritional_value}")

    if total_nutritional_value <= 30:  
        pet_dog.do_a_puppy_eyes()
    elif total_nutritional_value <= 100:
        pet_dog.do_a_trick()
    elif total_nutritional_value >= 100:
        pet_dog.do_an_oopsie()

#def consume_ingredients(owner, pet_dog):
    #if energy.owner 


def game_loop():
    start_game()
    owner, pet_dog = indentify(None, None)
    while True:
        input("Press enter to mix ingredients...")
        total_nutritional_value, ingredients_list = get_nutritional_value()
        mix_ingredients(owner, pet_dog, total_nutritional_value, ingredients_list)
        if pet_dog.check_win() or owner.check_lose():
            break
    print("Thanks for playing Kitchen Concoctions!")

game_loop()

#while True:
   

    #check if won, if true end
   # if human.check_win():
    #    break
    ##check if lose, if true end
   # if human.check_lose():
       # break
    
##USE FUNCTION CODES FOR ENERGY WHEN 0-20.... 
#energy_expense:
    ##you expend energy everytime you cook for your pet
    ##when your pet is low on energy it cannot perform tricks
    #if total energy for both of you ever = 0-10 u lose the game

##maybe later add actions or involve 3 different objects somehow

