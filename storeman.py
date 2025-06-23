# Contain all functions that cover handling of data storage
from filesman import *

INGREDIENT_FILENAME="ingredients.data"
RECIPE_FILENAME="recipes.data"

def add_ingredient(ingredient):
    append_to_store(ingredient,INGREDIENT_FILENAME)

# Returns ingredients as a list of strings, sorted
def get_sorted_ingredient_list():
    sorted_list =  []
    ingredients = read_dict_from_file(INGREDIENT_FILENAME)
    for item in ingredients:
        sorted_list.append(item["name"])
    sorted_list.sort()
    print(sorted_list)
    return sorted_list

def add_recipe(recipe):
    append_to_store(recipe,RECIPE_FILENAME)

# Appends a dictionary to a given list of dictionaries if it's not already stored there.
def append_to_store(new_object,filename):
    storelist = read_dict_from_file(filename)
    if not check_if_exists(storelist,new_object["name"]):
        storelist.append(new_object)
        write_dict_to_file(storelist,filename)

# Checks if any dict found in a list has the same value for name
def check_if_exists(list,search_string):
    for item in list:
        if search_string == item["name"]:
            return True
    return False