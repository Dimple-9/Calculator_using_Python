import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        calcuator = Calculator()
        self.assertEqual(calcuator.result, 4)


if __name__ == '__main__':
    unittest.main()