import os
from CocktailDB import CocktailDBAPI
import json
from relay import *

# def print_drink_names(json_response):
#     drinks = json_response['drinks']
#     for drink in drinks:
#         drink_name = drink['strDrink']
#         print(drink_name)


# API = CocktailDBAPI(os.getenv("API_KEY"))

# ingredient_list = API.get_ingredient_list()
# print(ingredient_list)

# random = API.get_random_cocktail()
# print(random)

# name = API.search_cocktails_by_name("sex on the beach")
# print_drink_names(name)

# by_list_ing = API.get_cocktails_by_list_of_ingredients("Gin,Vodka,Rum")
# print_drink_names(by_list_ing)

# Example usage
relay_data = [
    {"relay_number": 1, "duration": 3},  # Relay 1 will remain on for 3 seconds
    {"relay_number": 2, "duration": 5},  # Relay 2 will remain on for 5 seconds
    {"relay_number": 3, "duration": 2},  # Relay 3 will remain on for 2 seconds
]
relay = relay(relay_data)

relay.control_relays()
