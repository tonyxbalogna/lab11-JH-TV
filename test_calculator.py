import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(3, add(1,2))
        self.assertEqual(100, add(75, 25))
        self.assertEqual(5.2, add(3.2, 2))
    def test_subtract(self): # 3 assertions
        self.assertEqual(-1, subtract(1, 2))
        self.assertEqual(50, subtract(75, 25))
        self.assertEqual(1, subtract(3.2, 2.2))
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2), 6)
        self.assertEqual(mul(-1,2), -2)
        self.assertEqual(mul(1000,0), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10), 5)
        self.assertEqual(div(10,-2), -0.2)
        self.assertEqual(div(10,0), 0)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):# 1 assertion

        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(1, logarithm(10, 10))
        self.assertEqual(.5, logarithm(100, 10))
        self.assertEqual(3, logarithm(3, 27))

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 6)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertEqual(hypotenuse(-3,4), 5)
        self.assertEqual(hypotenuse(3,-4), 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(49), 7)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
