import requests
import string
import json

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

    json.dump(drinks, open("../drinks.json", "w"))

if __name__ == "__main__":
    update_local_db()
