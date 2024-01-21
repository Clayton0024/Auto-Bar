from abc import ABC, abstractmethod
from typing import Dict, List
from hardware_interface import HardwareInterface
from communication_interface import TcpCommunicator


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


class MessageError(Exception):
    pass

class IncomingMessage:
    def __init__(self, message: dict):
        self._message = message
        self._type = self._determine_type()

    def _determine_type(self):
        # Determine the type of the message based on its content
        if 'type' in self._message:
            return self._message['type']
        else:
            raise MessageError("Message dictionary must contain a 'type' key")

    @property
    def type(self):
        return self._type

    @property
    def content(self):
        return self._message


class Autobar(AutobarInterface):
    def __init__(self, hardware: HardwareInterface=None):
        self._available_ingredients: Dict[int, Ingredient] = {}  # TODO: Load from file if available

    def _set_available_drinks(self) -> None:
        # TODO: filter local database for drinks that can be made with available ingredients
        pass

    def _handle_set_ingredients_message(self, message: dict):
        ingredient_list: List[Ingredient] = []
        for ingredient in message['ingredients']:
            if 'name' not in ingredient:
                raise(MessageError('Ingredient must have a name'))
            if 'quantity_ml' not in ingredient:
                raise(MessageError('Ingredient must have a quantity in ml'))
            if 'relay_no' not in ingredient:
                raise(MessageError('Ingredient must have a relay number'))
            if 'abv_pct' not in ingredient:
                raise(MessageError('Ingredient must have an alcohol percentage'))
            if 'install_time_s' not in ingredient:
                raise(MessageError('Ingredient must have an install time'))
            
            relay_no = int(ingredient['relay_no'])
            if relay_no < 1 or relay_no > 16:
                raise(MessageError('Relay number must be between 1 and 16'))
            
            abv_pct = float(ingredient['abv_pct'])
            if abv_pct < 0 or abv_pct > 100:
                raise(MessageError('Alcohol percentage must be between 0 and 100'))

            ingredient_list.append(Ingredient(
                name=ingredient['name'],
                quantity_ml=ingredient['quantity_ml'],
                relay_no=relay_no,
                abv_pct=abv_pct,
                install_time_s=ingredient['install_time_s']
            ))

        self._set_ingredients(ingredient_list)

    def _handle_place_order_message(self, message: dict):
        if 'drink_id' not in message:
            raise(MessageError('Order must have a drink id'))
        if 'multiplier' not in message:
            raise(MessageError('Order must have a multiplier'))
        self.place_order(Order(
            id=0,
            drink_id=message['drink_id'],
            multiplier=message['multiplier']
        ))

    def _handle_get_available_ingredients_message(self, message: dict):
        self.send_message({
            'type': 'available_ingredients',
            'ingredients': self.get_available_ingredients()
        })
    
    def _handle_get_available_drinks_message(self, message: dict):
        self.send_message({
            'type': 'available_drinks',
            'drinks': self.get_available_drinks()
        })

    def _handle_get_status_message(self, message: dict):
        self.send_message({
            'type': 'status',
            'status': self.get_status()
        })

    def on_message_received(self, message: dict):
        msg = IncomingMessage(message)
        print("Received message: ")
        print(msg.content)
        if msg.type == 'set_ingredients':
            self._handle_set_ingredients_message(msg.content)
        elif msg.type == 'place_order':
            self._handle_place_order_message(msg.content)

    def get_available_drinks(self) -> List[Drink]:
        return self._available_drinks

    def get_available_ingredients(self) -> List[Ingredient]:
        return self._available_ingredients
    
    def set_ingredients(self, ingredients: List[Ingredient]):
        self._set_ingredients(ingredients)

    def _set_ingredients(self, ingredients: List[Ingredient]):
        self._available_ingredients.update({ingredient.relay_no: ingredient for ingredient in ingredients})

    def place_order(self, order: Order) -> bool:
        
        pass

    def get_status(self) -> str:
        pass