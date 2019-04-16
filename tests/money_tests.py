import unittest

from money.Dollar import Dollar
from money.Franc import Franc


class DollarTests(unittest.TestCase):

    def test_Multiplication(self):
        five = Dollar(5)
        self.assertEqual(Dollar(10), five.times(2))
        self.assertEqual(Dollar(15), five.times(3))

    def test_Franc_Multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality_of_dollar_objects(self):
        self.assertTrue(Dollar(5) == Dollar(5))
        self.assertTrue(Dollar(6) != Dollar(5))
