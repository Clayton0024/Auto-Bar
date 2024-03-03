import unittest
from cocktail_database import attempt_to_convert_to_ml


class TestCocktailDatabase(unittest.TestCase):
    def test_convert_to_ml(self):
        test_measurements = ["250 ml", "16 cl", "1/8 shot", "2 shots", "6 oz"]
        expected_results = [250, 160, 5, 88, 177]

        for idx, measurement in enumerate(test_measurements):
            res = attempt_to_convert_to_ml(measurement)
            self.assertEqual(res, f"{expected_results[idx]} ml")