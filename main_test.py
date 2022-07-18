import unittest
import main


class UnitTestLeastSquares(unittest.TestCase):
    
    def test_calculate_least_square(self):
        
        testY1 = main.Calculation
        testY2 = main.Calculation
        testY3 = main.Calculation
        testY4 = main.Calculation
        testError = main.Calculation


        self.assertEqual(testY1.calculate_least_square('y1'), 'y36', "Sollte xy rauskommen")
        self.assertEqual(testY2.calculate_least_square('y2'), 'y11', "Sollte xy rauskommen")
        self.assertEqual(testY3.calculate_least_square('y3'), 'y2', "Sollte xy rauskommen")
        self.assertEqual(testY4.calculate_least_square('y4'), 'y33', "Sollte xy rauskommen")
        
        
        with self.assertRaises(KeyError):
             testError.calculate_least_square('y64')   # geht nicht
        
   
    
"""      testY2 = main.Calculation
        result2 = testY2.calculate_least_square('y1')       
        self.assertEqual(result2, 'y36', "Sollte xy rauskommen")

        testY3 = main.Calculation
        result3 = testY3.calculate_least_square('y1')       
        self.assertEqual(result3, 'y36', "Sollte xy rauskommen")

        testY4 = main.Calculation
        result4 = testY4.calculate_least_square('y1')       
        self.assertEqual(result4, 'y36', "Sollte xy rauskommen")     """   
 

if __name__ == '__main__':
    unittest.main()
