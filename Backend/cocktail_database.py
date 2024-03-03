import requests
import string
import json
import os

from config import LOCAL_DRINK_DATABASE_FILEPATH
from objects import Drink, Ingredient, MeasuredIngredient


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
        if data["drinks"] is not None:
            for drink in data["drinks"]:
                drinks.append(drink)

    json.dump(drinks, open(LOCAL_DRINK_DATABASE_FILEPATH, "w"), indent=4, ensure_ascii=False)


def get_abv_pct(ingredient: str) -> float:
    # todo: implement a way to get the abv percentage of an ingredient
    return 0.0


def get_all_possible_ingredients() -> set[Ingredient]:
    if not os.path.exists(LOCAL_DRINK_DATABASE_FILEPATH):
        update_local_db()

    drinks = json.load(open(LOCAL_DRINK_DATABASE_FILEPATH, "r"))

    ingredients = set()

    for drink in drinks:
        for i in range(1, 16):
            ingredient = drink[f"strIngredient{i}"]
            if ingredient is not None and ingredient != "":
                ingredients.add(ingredient.lower())

    return [Ingredient(ingredient, get_abv_pct(ingredient)) for ingredient in ingredients]


def get_all_possible_measures() -> set[Ingredient]:
    if not os.path.exists(LOCAL_DRINK_DATABASE_FILEPATH):
        update_local_db()

    drinks = json.load(open(LOCAL_DRINK_DATABASE_FILEPATH, "r"))

    measures = set()

    for drink in drinks:
        for i in range(1, 16):
            measure = drink[f"strMeasure{i}"]
            if measure is not None and measure != "":
                measures.add(measure.lower())

    return [measure for measure in measures]


conversion_dict = {
    "oz": 29.5735,
    "cup": 240,
    "tbsp": 14.7868,
    "tsp": 4.92892,
    "shot": 44.3603,
    "shots": 44.3603,
    "ml": 1,
    "cl": 10,
    "l": 1000,
}


def attempt_to_convert_to_ml(input_str) -> str:
    # Try to extract the numeric value and the unit.
    try:
        # Split the input string to extract the numeric value and the unit.
        parts = input_str.split()
        if not parts:
            return input_str
        # Handle fractional quantities.
        if "/" in parts[0]:
            num_parts = parts[0].split("/")
            if len(num_parts) == 2:
                quantity = float(num_parts[0]) / float(num_parts[1])
            else:
                return input_str
        else:
            quantity = float(parts[0])

        # Identify the unit and convert to lowercase for consistency.
        unit = parts[1].lower()

        # Check if the unit is in the dictionary and perform the conversion.
        if unit in conversion_dict:
            return f"{int(quantity * conversion_dict[unit])} ml"
        else:
            return input_str
    except (ValueError, IndexError, AttributeError):
        # Return None if there's an error in conversion.
        return input_str


def get_all_possible_drinks() -> set[Drink]:
    if not os.path.exists(LOCAL_DRINK_DATABASE_FILEPATH):
        update_local_db()

    drinks = json.load(open(LOCAL_DRINK_DATABASE_FILEPATH, "r"))

    drink_set = []

    for drink in drinks:
        ingredients: list[MeasuredIngredient] = []
        for i in range(1, 16):
            ingredient = drink[f"strIngredient{i}"]
            measure = drink[f"strMeasure{i}"]
            if measure is not None and measure != "":
                measure = attempt_to_convert_to_ml(measure)
            else:
                measure = "unknown"

            if ingredient is not None and ingredient != "":
                ingredients.append(
                    MeasuredIngredient(ingredient.lower(), measure, get_abv_pct(ingredient))
                )

        drink_set.append(
            Drink(
                id=drink["idDrink"],
                name=drink["strDrink"],
                ingredients=ingredients,
                description=drink["strInstructions"],
            )
        )

    return drink_set


def get_all_measurements():
    drinks = get_all_possible_drinks()
    measures = set()
    for drink in drinks:
        for ingredient in drink["ingredients"]:
            measures.add(ingredient["quantity_ml"])

    return measures


if __name__ == "__main__":
    # drinks = get_all_possible_drinks()
    ingredients = get_all_possible_ingredients()
    measures = get_all_measurements()
    for measure in measures:
        print(measure)
