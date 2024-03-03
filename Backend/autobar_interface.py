from abc import ABC, abstractmethod
import logging
from typing import Dict, List
import json
import os

from objects import AutobarIngredient, Drink, Order


class AutobarInterface(ABC):
    @abstractmethod
    def get_available_drinks(self) -> List[Drink]:
        """Get a list of available drinks."""
        pass

    @abstractmethod
    def get_available_ingredients(self) -> List[AutobarIngredient]:
        """Gets a list of available ingredients."""
        pass

    @abstractmethod
    def set_ingredients(self, ingredients: List[AutobarIngredient]):
        """
        Set the available ingredients with their quantities and location.
        ingredients must be a dictionary with keys:
            name: str
            quantity: int
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


class MessageError(Exception):
    pass


class IncomingMessage:
    def __init__(self, message: dict):
        self._message = message
        self._type = self._determine_type()

    def _determine_type(self):
        # Determine the type of the message based on its content
        if "type" in self._message:
            return self._message["type"]
        else:
            raise MessageError("Message dictionary must contain a 'type' key")

    @property
    def type(self):
        return self._type

    @property
    def content(self):
        return self._message


class Autobar(AutobarInterface):
    def __init__(self, ingredients_filepath="ingredients.json"):
        self._drink_database_filepath = "../drinks.json"

        self._available_ingredients: Dict[int, AutobarIngredient] = {}
        self._available_drinks = []  # Drinks that can be made with available ingredients
        self._full_ingredients_list = []  # All ingredients in database
        self._full_drink_list = self._load_drinks()  # All drinks in database

        self._ingredients_filepath = ingredients_filepath

        # load ingredients from file
        if os.path.exists(self._ingredients_filepath):
            self._load_ingredients_from_file()
        logging.info(f"Loaded ingredients from {self._ingredients_filepath}")
        logging.info(f"Available ingredients: {self._available_ingredients}")

    def _load_drinks(self):
        with open(self._drink_database_filepath, "r") as f:
            return json.load(f)

    def _can_make_drink(self, drink: Drink) -> bool:
        """
        Check if the ingredients for a drink are available.
        Returns:
            bool: True if the ingredients are available, False otherwise.
        """
        # todo: implement this
        return False

    def update_available_drinks(self) -> None:
        """
        Update list of available drinks based on the available ingredients in this Autobar instance.
        """
        self._available_drinks = []
        for drink in self._full_drink_list:
            if self._can_make_drink(drink):
                self._available_drinks.append(drink)

    def _save_ingredients_to_file(self):
        with open(self._ingredients_filepath, "w") as f:
            json.dump(self._available_ingredients, f)
            logging.info(f"Saved ingredients to {self._ingredients_filepath}")

    def _load_ingredients_from_file(self):
        with open(self._ingredients_filepath, "r") as f:
            json_ingredients = json.load(f)
            for idx, ingredient in enumerate(json_ingredients):
                self._available_ingredients.update(
                    {
                        int(idx): AutobarIngredient(
                            name=ingredient["name"],
                            quantity=ingredient["quantity"],
                            relay_no=ingredient["relay_no"],
                            abv_pct=ingredient["abv_pct"],
                            install_time_s=ingredient["install_time_s"],
                        )
                    }
                )

    def _handle_set_ingredients_message(self, message: dict):
        ingredient_list: List[AutobarIngredient] = []
        for ingredient in message["ingredients"]:
            if "name" not in ingredient:
                raise (MessageError("Ingredient must have a name"))
            if "quantity" not in ingredient:
                raise (MessageError("Ingredient must have a quantity in ml"))
            if "relay_no" not in ingredient:
                raise (MessageError("Ingredient must have a relay number"))
            if "abv_pct" not in ingredient:
                raise (MessageError("Ingredient must have an alcohol percentage"))
            if "install_time_s" not in ingredient:
                raise (MessageError("Ingredient must have an install time"))

            relay_no = int(ingredient["relay_no"])
            if relay_no < 1 or relay_no > 16:
                raise (MessageError("Relay number must be between 1 and 16"))

            abv_pct = float(ingredient["abv_pct"])
            if abv_pct < 0 or abv_pct > 100:
                raise (MessageError("Alcohol percentage must be between 0 and 100"))

            ingredient_list.append(
                AutobarIngredient(
                    name=ingredient["name"],
                    quantity=ingredient["quantity"],
                    relay_no=relay_no,
                    abv_pct=abv_pct,
                    install_time_s=ingredient["install_time_s"],
                )
            )

        self._set_ingredients(ingredient_list)

    def _handle_place_order_message(self, message: dict):
        if "drink_id" not in message:
            raise (MessageError("Order must have a drink id"))
        if "multiplier" not in message:
            raise (MessageError("Order must have a multiplier"))
        self.place_order(
            Order(id=0, drink_id=message["drink_id"], multiplier=message["multiplier"])
        )

    def _handle_get_available_ingredients_message(self, message: dict):
        self.send_message(
            {"type": "available_ingredients", "ingredients": self.get_available_ingredients()}
        )

    def _handle_get_available_drinks_message(self, message: dict):
        self.send_message({"type": "available_drinks", "drinks": self.get_available_drinks()})

    def _handle_get_status_message(self, message: dict):
        self.send_message({"type": "status", "status": self.get_status()})

    def on_message_received(self, message: dict):
        logging.info(f"Received message: {message}")
        msg = IncomingMessage(message)
        if msg.type == "set_ingredients":
            self._handle_set_ingredients_message(msg.content)
        elif msg.type == "place_order":
            self._handle_place_order_message(msg.content)

    def get_available_drinks(self) -> List[Drink]:
        """
        Get a list of available drinks.
        Returns:
            List[Drink]: A list of available drinks.
        """
        return self._available_drinks

    def get_available_ingredients(self) -> Dict[int, AutobarIngredient]:
        """
        Get a list of available ingredients.
        Returns:
            Dict[int, Ingredient]: A dictionary of available ingredients, indexed by relay number.
        """
        return self._available_ingredients

    def set_ingredients(self, ingredients: List[AutobarIngredient]):
        """
        Set the available ingredients with their quantities and location.
        ingredients must be a dictionary with keys:
            name: str
            quantity: int
            relay_no: int
        """
        self._set_ingredients(ingredients)

    def _set_ingredients(self, ingredients: List[AutobarIngredient]):
        for ingredient in ingredients:
            self._available_ingredients.update({ingredient["relay_no"]: ingredient})

        self._save_ingredients_to_file()

    def place_order(self, order: Order) -> bool:
        """
        Make a drink by name if ingredients are available.
        Returns:
            bool: True if the drink was successfully made, False otherwise.
        """
        logging.info(f"Placing order: {order}")
        pass

    def get_status(self) -> str:
        pass
