import os
import unittest
from autobar_interface import Autobar, AutobarIngredient
import tempfile


class TestAutobar(unittest.TestCase):
    def test_on_message_received_set_ingredients(self):
        with tempfile.TemporaryDirectory() as f:
            ingredients_path = f + "/ingredients.json"
            autobar = Autobar(ingredients_filepath=ingredients_path)
            # Mock message to be received
            test_message = {
                "type": "set_ingredients",
                "ingredients": [
                    {
                        "name": "Vodka",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 1,
                        "install_time_s": 1234567890,
                    }
                ],
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[1], AutobarIngredient)
            self.assertEqual(available_ingredients[1]["name"], "Vodka")
            self.assertEqual(available_ingredients[1]["quantity"], 500)
            self.assertEqual(available_ingredients[1]["abv_pct"], 40.0)
            self.assertEqual(available_ingredients[1]["relay_no"], 1)
            self.assertEqual(available_ingredients[1]["install_time_s"], 1234567890)

            # now let's try resetting that relay no
            test_message = {
                "type": "set_ingredients",
                "ingredients": [
                    {
                        "name": "Gin",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 1,
                        "install_time_s": 1234567890,
                    }
                ],
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[1], AutobarIngredient)
            self.assertEqual(available_ingredients[1]["name"], "Gin")

            # now let's try adding two ingredients to relay no 2 and 3
            test_message = {
                "type": "set_ingredients",
                "ingredients": [
                    {
                        "name": "Rum",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 2,
                        "install_time_s": 1234567890,
                    },
                    {
                        "name": "Whiskey",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 3,
                        "install_time_s": 1234567890,
                    },
                ],
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[2], AutobarIngredient)
            self.assertEqual(available_ingredients[2]["name"], "Rum")
            self.assertIsInstance(available_ingredients[3], AutobarIngredient)
            self.assertEqual(available_ingredients[3]["name"], "Whiskey")

    def test_on_message_received_relay_num_out_of_bounds(self):
        with tempfile.TemporaryDirectory() as f:
            ingredients_path = f + "/ingredients.json"
            autobar = Autobar(ingredients_filepath=ingredients_path)

            # ingredient of relay no 0 should fail
            test_message = {
                "type": "set_ingredients",
                "ingredients": [
                    {
                        "name": "Vodka",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 0,
                        "install_time_s": 1234567890,
                    }
                ],
            }

            # Simulate receiving a message
            with self.assertRaises(Exception):
                autobar.on_message_received(test_message)

            # ingredient of relay no 17 should fail
            test_message = {
                "type": "set_ingredients",
                "ingredients": [
                    {
                        "name": "Vodka",
                        "quantity": 500,
                        "abv_pct": 40.0,
                        "relay_no": 17,
                        "install_time_s": 1234567890,
                    }
                ],
            }

            with self.assertRaises(Exception):
                autobar.on_message_received(test_message)

    def test_load_existing_ingredients(self):
        ingredients_path = "./utilities/ingredients_mojito_margarita.json"
        # ensure this file exists
        self.assertTrue(os.path.exists(ingredients_path))
        autobar = Autobar(ingredients_filepath=ingredients_path)

        # Check if the ingredients are correctly loaded
        available_ingredients = autobar.get_available_ingredients()
        self.assertIsInstance(available_ingredients[0], AutobarIngredient)
        self.assertEqual(available_ingredients[0]["name"], "Tequila")
        self.assertEqual(available_ingredients[0]["quantity"], "500")
        self.assertEqual(available_ingredients[0]["abv_pct"], 40.0)
        self.assertEqual(available_ingredients[0]["relay_no"], 1)
        self.assertEqual(available_ingredients[0]["install_time_s"], 1234567890)

        self.assertIsInstance(available_ingredients[1], AutobarIngredient)
        self.assertEqual(available_ingredients[1]["name"], "Triple sec")
        self.assertEqual(available_ingredients[1]["quantity"], "500")
        self.assertEqual(available_ingredients[1]["abv_pct"], 20.0)
        self.assertEqual(available_ingredients[1]["relay_no"], 2)
        self.assertEqual(available_ingredients[1]["install_time_s"], 1234567890)

        self.assertIsInstance(available_ingredients[8], AutobarIngredient)
        self.assertEqual(available_ingredients[8]["name"], "Soda Water")
        self.assertEqual(available_ingredients[8]["quantity"], "500")
        self.assertEqual(available_ingredients[8]["abv_pct"], 0.0)
        self.assertEqual(available_ingredients[8]["relay_no"], 9)
        self.assertEqual(available_ingredients[8]["install_time_s"], 1234567890)

    # in progress
    # def test_get_available_drinks(self):
    #     ingredients_path = './utilities/ingredients_mojito_margarita.json'
    #     autobar = Autobar(ingredients_filepath=ingredients_path)

    #     # we'll assume drinks are correctly loaded due to other tests
    #     available_drinks = autobar.get_available_drinks()

    #     # assert that Mojito is in the list of available drinks
    #     self.assertIn('Mojito', available_drinks)

    #     # assert that Margarita is in the list of available drinks
    #     self.assertIn('Margarita', available_drinks)


if __name__ == "__main__":
    unittest.main()
