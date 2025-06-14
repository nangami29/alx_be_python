import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
         """Set up the SimpleCalculator instance before each test."""
         self.calc= SimpleCalculator()
    
        
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(5, 7), 12)
    
    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 7), -2)
        self.assertEqual(self.calc.subtract(-5, 7), 12)
        self.assertEqual(self.calc.subtract(10, 7), -2)
    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5 * 7), 35)
        self.assertEqual(self.calc.multiply(-5 * 7), -35)
        self.assertEqual(self.calc.multiply(-5 * -7), 35)


    def test_divide(self):
        """Test the division method."""
        
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(12, 5), 2.4)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
   TestSimpleCalculator()


