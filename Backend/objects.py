from typing import List

class Ingredient(dict):
    """
    An Ingredient is a dictionary with properties:
        name: str
        abv_pct: float
    """

    def __init__(self, name: str, abv_pct: float):
        super().__init__(name=name, abv_pct=abv_pct)


class MeasuredIngredient(Ingredient):
    """
    A MeasuredIngredient is a dictionary with properties:
        name: str
        quantity_ml: int
        abv_pct: float
    """

    def __init__(self, name: str, quantity_ml: int, abv_pct: float):
        super().__init__(name=name, abv_pct=abv_pct)
        self['quantity_ml'] = quantity_ml


class AutobarIngredient(MeasuredIngredient):
    """
    An AutobarIngredient is a dictionary with properties:
        name: str
        quantity_ml: int
        abv_pct: float
        relay_no: int
        install_time_s: int   (unix timestamp)
    """

    def __init__(self, name: str, quantity_ml: int, abv_pct: float, relay_no: int, install_time_s: int):
        super().__init__(name=name, quantity_ml=quantity_ml, abv_pct=abv_pct)
        self['relay_no'] = relay_no
        self['install_time_s'] = install_time_s

class Drink(dict):
    """
    A drink is a dictionary consisting of:
        id: int
        name: str
        ingredients: List[Ingredient]
        description: str
    """

    def __init__(self, id: int, name: str, ingredients: List[AutobarIngredient], description: str):
        super().__init__(id=id, name=name, ingredients=ingredients, description=description)


class Order(dict):
    """
    An order is a dictionary consisting of:
        id: int
        drink_id: int
        multiplier: float
    """

    def __init__(self, id: int, drink_id: int, multiplier: float):
        super().__init__(id=id, drink_id=drink_id, multiplier=multiplier)


