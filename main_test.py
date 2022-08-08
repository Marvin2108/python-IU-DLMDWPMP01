import unittest
import main
from main import RangeError


class UnitTestLeastSquares(unittest.TestCase):
    
    def test_calculate_least_square(self):
        
        testY1 = main.LeastSquareMethod('y1')
        testY2 = main.LeastSquareMethod('y2')
        testY3 = main.LeastSquareMethod('y3')
        testY4 = main.LeastSquareMethod('y4')
        
        self.assertEqual(testY1.calculate_least_square(testY1.trainingNumber), 'y36', "Sollte y36 rauskommen")
        self.assertEqual(testY2.calculate_least_square(testY2.trainingNumber), 'y11', "Sollte y11 rauskommen")
        self.assertEqual(testY3.calculate_least_square(testY3.trainingNumber), 'y2' , "Sollte y2 rauskommen")
        self.assertEqual(testY4.calculate_least_square(testY4.trainingNumber), 'y33', "Sollte y33 rauskommen")
        
        testError = main.LeastSquareMethod('y18') # should raise Error
                
        with self.assertRaises(RangeError):
             testError.calculate_least_square(testError.trainingNumber)

    def test_test_function (self):
        
        main.main()
        self.assertIsNotNone(main.test_function()) # checks if returned value is not empty


if __name__ == '__main__':
    unittest.main()
