import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_addd(self):
        self.assertEqual(self.calc.add(5, 2), 7)

    def test_adddd(self):
        self.assertEqual(self.calc.add(6 , 2) , 8 )
    
    def test_sub(self):
        self.assertEqual(self.calc.subtract(5 , 4 ) , 1)
    

    def test_subb(self):
        self.assertEqual(self.calc.subtract(6 , 2 ) , 4)
    
    def test_multi(self):
        self.assertEqual(self.calc.multiply(5 , 5 ) , 25)
    
    def test_multii(self):
        self.assertEqual(self.calc.multiply(3 , 7 ) , 21 )
    
    def test_divi(self):
        self.assertEqual(self.calc.divide(4, 2 ) , 2 )
    
    def test_divii(self):
        self.assertEqual(self.calc.divide(6 , 2 ) , 3)
    
    def test_modu(self):
        self.assertEqual(self.calc.modulo(5 , 2 ) , 1)
    
    def test_moduu(self):
        self.assertEqual(self.calc.modulo(18 , 9 ) , 0)

        
if __name__ == '__main__':
    unittest.main()    