from abc import ABC, abstractmethod
from typing import List


class Ingredient(dict):
    """
    An ingredient is a dictionary with properties:
        name: str
        quantity_ml: int
        abv_pct: float
        relay_no: int
        install_time_s: int   (unix timestamp)
    """

    def __init__(
        self, name: str, quantity_ml: int, abv_pct: float, relay_no: int, install_time_s: int
    ):
        super().__init__(
            name=name,
            quantity_ml=quantity_ml,
            abv_pct=abv_pct,
            relay_no=relay_no,
            install_time_s=install_time_s,
        )


class Drink(dict):
    """
    A drink is a dictionary consisting of:
        id: int
        name: str
        ingredients: List[Ingredient]
        description: str
    """

    def __init__(self, id: int, name: str, ingredients: List[Ingredient], description: str):
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


class AutobarInterface(ABC):
    @abstractmethod
    def get_available_drinks(self) -> List[Drink]:
        """Get a list of available drinks."""
        pass

    @abstractmethod
    def get_available_ingredients(self) -> List[Ingredient]:
        """Gets a list of available ingredients."""
        pass

    @abstractmethod
    def set_ingredients(self, ingredients: List[Ingredient]):
        """
        Set the available ingredients with their quantities and location.
        ingredients must be a dictionary with keys:
            name: str
            quantity_ml: int
            relay_no: int
        """
        pass

    @abstractmethod
    def place_order(self, order: Order) -> bool:
        """Make a drink by name if ingredients are available.
        Returns:
            bool: True if the drink was successfully made, False otherwise.
        """
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Get the status or information about the hardware system."""
        pass
