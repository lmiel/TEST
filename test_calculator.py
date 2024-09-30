import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        
    def test_add_method(self):
        result = self.calc.add(1, 3)
        self.assertEqual(4, result)

    def test_subtract_method(self):
        result = self.calc.subtract(4, 2)
        self.assertEqual(2, result)
        result = self.calc.subtract(2, 0)
        self.assertEqual(2, result)
        result = self.calc.subtract(1, 6)
        self.assertEqual(-5, result)
        
    def test_multiply_method(self):
        result = self.calc.multiply(2, 3)
        self.assertEqual(6, result)
        result = self.calc.multiply(2, 0)
        self.assertEqual(0, result)
        result = self.calc.multiply(2, -3)
        self.assertEqual(-6, result)

    
    def test_divide_method(self):
        result = self.calc.divide(6, 3)
        self.assertEqual(2, result)
        result = self.calc.divide(6, 0)
        self.assertEqual('undefined', result)
        result = self.calc.divide(6, -3)
        self.assertEqual(-2, result)
        result = self.calc.divide(4, 16)
        self.assertEqual(0.25, result)
        
    def test_power_method(self):
        result = self.calc.power(2, 3)
        self.assertEqual(8, result)
        result = self.calc.power(2, 0)
        self.assertEqual(1, result)
        result = self.calc.power(2, -3)
        self.assertEqual(0.125, result)
        result = self.calc.power(0, 0)
        self.assertEqual(1, result)
        result = self.calc.power(1, 3)
        self.assertEqual(1, result)
    
    def test_factorial_method(self):
        result = self.calc.factorial(5)
        self.assertEqual(120, result)
        result = self.calc.factorial(0)
        self.assertEqual(1, result)
        result = self.calc.factorial(1)
        self.assertEqual(1, result)
        result = self.calc.factorial(-3)
        self.assertEqual(-6, result)


