# Write your solution here

def file_to_recipes(filename: str):
    recipes = []    
    recipe = []
    with open(filename) as file:    
        for line in file:            
            if line == "\n":
                recipes.append(recipe)
                recipe = []
                continue
            else:
                recipe.append(line.strip())
        recipes.append(recipe)    

    return recipes


def search_by_name(filename: str, word: str):
    recipes = file_to_recipes(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe[0].lower():
            found.append(recipe[0])

    return found        


def search_by_time(filename: str, prep_time: int):
    recipes = file_to_recipes(filename)
    found = []
    for recipe in recipes:
        if prep_time >= int(recipe[1]):
            found.append(f"{recipe[0]}, preparation time {recipe[1]} min")

    return found


def search_by_ingredient(filename: str, ingredient: str):
    recipes = file_to_recipes(filename)
    found = []
    for recipe in recipes:
        for i in range(2, len(recipe)):
            if ingredient.lower() in recipe[i].lower():
                found.append(f"{recipe[0]}, preparation time {recipe[1]} min")
                break

    return found
















