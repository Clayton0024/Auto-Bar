import requests


class CocktailDBAPI:
    def __init__(self, api_key: int):
        self.base_url = f"https://www.thecocktaildb.com/api/json/v2/{api_key}"

    def search_cocktails_by_name(self, search_term: str):
        endpoint = f"{self.base_url}/search.php?s={search_term}"
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
        # ingredients should be a comma seperated string of ingredents" Example: Gin,Vodka,Dry_Vermouth
        endpoint = f"{self.base_url}/filter.php?i={ingredients}"
        response = requests.get(endpoint)
        data = response.json()
        return data
