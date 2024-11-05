import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):

    def test_calculate_valid_input(self):
        input_data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        expected_output = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        output = calculate(input_data)
        self.assertEqual(output, expected_output)

    def test_calculate_invalid_input_length(self):
        input_data = [1, 2, 3]
        with self.assertRaises(ValueError) as context:
            calculate(input_data)
        self.assertEqual(str(context.exception), "List must contain nine numbers.")

if __name__ == '__main__':
    unittest.main()