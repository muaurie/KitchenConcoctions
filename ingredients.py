from treat import Treat
import random

class Ingredients:
    ingredients_list = [
        ("Bleach", 0),
        ("Tofu", 15),
        ("Dish Soap", 5),
        ("ABS Plastic", 0),
        ("Fish Scales", 5),
        ("Beef Tongue", 20),
        ("Water", 30),
        ("Dirt", 15),
        ("Sodium Chloride", 5),
        ("Bricks", 10),
        ("Cinnamon", 5),
        ("Apple", 15),
        ("Spaghetti", 25),
        ("Whey Protein", 50),
        ("Cooked Chicken", 35),
        ("Rye Bread", 30),
        ("Lettuce", 10),
        ("Tomato", 15),
        ("Sashimi Tuna", 30),
        ("Lentils", 40),
        ("Superfood Salad", 80),
        ("Ultraviolet Waves", 5),
        ("Whole Coffee Beans", 10),
        ("Curry Sauce",30),
        ("Tomatillos", 10),
        ("Diced Onion", 10)
    ]

    ingredients = [Treat(name, nutritional_value) for name, nutritional_value in ingredients_list]
#get 3 random sample from ingredients list)
def get_random_ing():
        return random.sample(Ingredients.ingredients, 3)
#add them together and return their value
def cook_ingredients(ingredients):
      total_val = sum(ingredient.nutritional_value for ingredient in ingredients)
      return total_val
##save get_random_ing() in random_ingredients
random_ingredients = get_random_ing()
#function for getting total
total_nutritional_value = cook_ingredients(random_ingredients)

print("Random Ingredients:")
for ingredient in random_ingredients:
    print(f"{ingredient.name}: {ingredient.nutritional_value}")

print(f"Total Nutritional Value: {total_nutritional_value}")

