import unittest
import main


class UnitTestLeastSquares(unittest.TestCase):
    def test_least_squares_y1(self):
        result = main.calculateSumSquareY1()
        self.assertEqual(result, 33.71178854422821, "Sollte xy rauskommen")


if __name__ == '__main__':
    unittest.main()
