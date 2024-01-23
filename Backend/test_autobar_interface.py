import unittest
from autobar_interface import Autobar, Ingredient
import tempfile

class TestAutobar(unittest.TestCase):
    def test_on_message_received_set_ingredients(self):
        with tempfile.TemporaryDirectory() as f:
            ingredients_path = f + '/ingredients.json'
            autobar = Autobar(hardware=None, ingredients_filepath=ingredients_path)
            # Mock message to be received
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Vodka',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 1,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[1], Ingredient)
            self.assertEqual(available_ingredients[1]['name'], 'Vodka')
            self.assertEqual(available_ingredients[1]['quantity_ml'], 500)
            self.assertEqual(available_ingredients[1]['abv_pct'], 40.0)
            self.assertEqual(available_ingredients[1]['relay_no'], 1)
            self.assertEqual(available_ingredients[1]['install_time_s'], 1234567890)


            # now let's try resetting that relay no
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Gin',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 1,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[1], Ingredient)
            self.assertEqual(available_ingredients[1]['name'], 'Gin')

            # now let's try adding two ingredients to relay no 2 and 3
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Rum',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 2,
                        'install_time_s': 1234567890
                    },
                    {
                        'name': 'Whiskey',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 3,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Check if the ingredients are correctly updated
            available_ingredients = autobar.get_available_ingredients()
            self.assertIsInstance(available_ingredients[2], Ingredient)
            self.assertEqual(available_ingredients[2]['name'], 'Rum')
            self.assertIsInstance(available_ingredients[3], Ingredient)
            self.assertEqual(available_ingredients[3]['name'], 'Whiskey')


    def test_on_message_received_relay_no_oob(self):
        with tempfile.TemporaryDirectory() as f:
            ingredients_path = f + '/ingredients.json'
            autobar = Autobar(hardware=None, ingredients_filepath=ingredients_path)

            # ingredient of relay no 0 should fail
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Vodka',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 0,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            with self.assertRaises(Exception):
                autobar.on_message_received(test_message)

            # ingredient of relay no 17 should fail
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Vodka',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 17,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            with self.assertRaises(Exception):
                autobar.on_message_received(test_message)

    def test_load_existing_ingredients(self):
        with tempfile.TemporaryDirectory() as f:
            ingredients_path = f + '/ingredients.json'
            autobar = Autobar(hardware=None, ingredients_filepath=ingredients_path)
            # we need to ensure we can read our own file, so we need to write it first
            test_message = {
                'type': 'set_ingredients',
                'ingredients': [
                    {
                        'name': 'Vodka',
                        'quantity_ml': 500,
                        'abv_pct': 40.0,
                        'relay_no': 1,
                        'install_time_s': 1234567890
                    }
                ]
            }

            # Simulate receiving a message
            autobar.on_message_received(test_message)

            # Create an instance of Autobar with the same temp file
            autobar_2 = Autobar(hardware=None, ingredients_filepath=ingredients_path)

            # Check if the ingredients are correctly loaded
            available_ingredients = autobar_2.get_available_ingredients()
            print(available_ingredients)
            self.assertIsInstance(available_ingredients[1], Ingredient)
            self.assertEqual(available_ingredients[1]['name'], 'Vodka')
            self.assertEqual(available_ingredients[1]['quantity_ml'], 500)
            self.assertEqual(available_ingredients[1]['abv_pct'], 40.0)
            self.assertEqual(available_ingredients[1]['relay_no'], 1)
            self.assertEqual(available_ingredients[1]['install_time_s'], 1234567890)

if __name__ == '__main__':
    unittest.main()
