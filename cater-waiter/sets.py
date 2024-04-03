"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    nuevo_set=set()
    for ingrediente in dish_ingredients:
        nuevo_set.add(ingrediente)
    salida=(dish_name,nuevo_set)
    return (salida)

def check_drinks(drink_name, drink_ingredients):
    drink_ingredients=set(drink_ingredients)
    if(len(drink_ingredients.intersection(ALCOHOLS))>0):
        return drink_name+" Cocktail"   
    else:
        return drink_name+" Mocktail"  


    


def categorize_dish(dish_name, dish_ingredients):
    
    """Categorize `dish_name` based on `dish_ingredients`.

    :param dish_name: str - dish to be categorized.
    :param dish_ingredients: list - ingredients for the dish.
    :return: str - the dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`

    """
    dish_ingredients=set(dish_ingredients)
    if(dish_ingredients.issubset(VEGAN)==True):
        return dish_name+ ": VEGAN"
    elif (dish_ingredients.issubset(VEGETARIAN)==True):
        return dish_name+ ": VEGETARIAN"
    
    elif (dish_ingredients.issubset(PALEO)==True):
        return dish_name+ ": PALEO"
    
    elif (dish_ingredients.issubset(KETO)==True):
        return dish_name+ ": KETO"
    
    elif (dish_ingredients.issubset(OMNIVORE)==True):
        return dish_name+ ": OMNIVORE"
    


def tag_special_ingredients(dish):

    dish_name,dish_ingredients=dish
    dish_ingredients=set(dish_ingredients)
    return (dish_name,dish_ingredients.intersection(SPECIAL_INGREDIENTS))
    


def compile_ingredients(dishes):


    superSET=set()
    for dish in dishes:
        superSET=superSET.union(dish)
    return superSET
    


def separate_appetizers(dishes, appetizers):

    newDishes=set(dishes)
    newAppetizers=set(appetizers)

    newList= newDishes.difference(newAppetizers)
    return list(newList)
    


def singleton_ingredients(dishes, intersection):
    
    superSet=set()
    auxIntersection=set(intersection)
    for dish in dishes:
        superSet=superSet.union(set(dish).difference(auxIntersection))
        
    return superSet


