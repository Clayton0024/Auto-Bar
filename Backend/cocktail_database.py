import requests
import string
import json
import os

from config import LOCAL_DRINK_DATABASE_FILEPATH
from objects import Drink, Ingredient

class CocktailDBAPI:
    def __init__(self, api_key: int):
        self.base_url = f"https://www.thecocktaildb.com/api/json/v2/{api_key}"

    def search_cocktails_by_name(self, search_term: str):
        endpoint = f"{self.base_url}/search.php?s={search_term}"
        response = requests.get(endpoint)
        data = response.json()
        return data
    
    def search_cocktails_by_first_letter(self, first_letter: str):
        endpoint = f"{self.base_url}/search.php?f={first_letter}"
        response = requests.get(endpoint)
        data = response.json()
        return data

    def get_ingredient_list(self):
        endpoint = f"{self.base_url}/list.php?i=list"
        response = requests.get(endpoint)
        data = response.json()
        return data

    def get_random_cocktail(self):
        endpoint = f"{self.base_url}/random.php"
        response = requests.get(endpoint)
        data = response.json()
        return data

    def get_cocktails_by_list_of_ingredients(self, ingredients: str):
        endpoint = f"{self.base_url}/filter.php?i={ingredients}"
        response = requests.get(endpoint)
        data = response.json()
        return data

def update_local_db():
    drinks = []
    alphabet = string.ascii_lowercase  # Get all lowercase letters
    api = CocktailDBAPI("1")
    for letter in alphabet:
        print(f"Getting drinks starting with {letter}")
        data = api.search_cocktails_by_first_letter(letter)
        if data['drinks'] is not None:
            for drink in data['drinks']:
                drinks.append(drink)

    json.dump(drinks, open(LOCAL_DRINK_DATABASE_FILEPATH, "w"))

def get_abv_pct(ingredient: str) -> float:
    #todo: implement a way to get the abv percentage of an ingredient
    return 0.0

def get_all_possible_ingredients() -> set[Ingredient]:
    if not os.path.exists(LOCAL_DRINK_DATABASE_FILEPATH):
        update_local_db()

    drinks = json.load(open(LOCAL_DRINK_DATABASE_FILEPATH, "r"))

    ingredients = []

    for drink in drinks:
        for i in range(1, 16):
            ingredient = drink[f"strIngredient{i}"]
            if ingredient is not None and ingredient != "" and ingredient.lower() not in ingredients:
                ingredients.append(Ingredient(ingredient.lower(), get_abv_pct(ingredient)))

    return ingredients

def get_all_possible_drinks() -> set[Drink]:
    if not os.path.exists(LOCAL_DRINK_DATABASE_FILEPATH):
        update_local_db()

    drinks = json.load(open(LOCAL_DRINK_DATABASE_FILEPATH, "r"))

    drink_set = []

    for drink in drinks:
        drink_set.append(Drink(
            id=drink['idDrink'],
            name=drink['strDrink'],
            ingredients=[
                Ingredient(drink[f"strIngredient{i}"].lower(), get_abv_pct(drink[f"strIngredient{i}"]))
                for i in range(1, 16)
                if drink[f"strIngredient{i}"] is not None and drink[f"strIngredient{i}"] != ""
            ],
            description=drink['strInstructions']
        ))

    return drink_set


if __name__ == "__main__":
    drinks = get_all_possible_drinks()
    ingredients = get_all_possible_ingredients()
