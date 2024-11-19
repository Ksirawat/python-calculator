import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add32int(self):
        self.assertEqual(self.calc.add(2147483647,1),2147483648)
    def test_add32int1(self):
        self.assertEqual(self.calc.add(-2147483648,-1),-2147483649)

    def test_sub_1(self):
        self.assertEqual(self.calc.subtract(5,3),2)
    def test_sub_2(self):
        self.assertEqual(self.calc.subtract(3,5),-2)
    
    def test_multi_1(self):
        self.assertEqual(self.calc.multiply(2,3),6)
    def test_multi_2(self):
        self.assertEqual(self.calc.multiply(3,2),6)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(10,2),5)
    def test_divide_2(self):
        self.assertEqual(self.calc.divide(10,3),3)
    
    def test_mod_1(self):
        self.assertEqual(self.calc.modulo(10,3),1)
    def test_mod_2(self):
        self.assertEqual(self.calc.modulo(15,4),3)

if __name__ == '__main__':
    unittest.main()