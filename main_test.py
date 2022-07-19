import unittest
import main

class UnitTestLeastSquares(unittest.TestCase):
    
    def test_calculate_least_square(self):
        
        testY1 = main.Calculation
        testY2 = main.Calculation
        testY3 = main.Calculation
        testY4 = main.Calculation
        testError = main.Calculation


        self.assertEqual(testY1.calculate_least_square('y1'), 'y36', "Sollte y36 rauskommen")
        self.assertEqual(testY2.calculate_least_square('y2'), 'y11', "Sollte y11 rauskommen")
        self.assertEqual(testY3.calculate_least_square('y3'), 'y2' , "Sollte y2 rauskommen")
        self.assertEqual(testY4.calculate_least_square('y4'), 'y33', "Sollte y33 rauskommen")
        
        
        with self.assertRaises(main.RangeError):
             testError.calculate_least_square('y64')   # geht nicht

    def test_test_function (self):
        main.main()
        self.assertIsNotNone(main.test_function())

 

if __name__ == '__main__':
    unittest.main()
