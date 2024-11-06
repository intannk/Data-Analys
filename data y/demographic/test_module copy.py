import unittest
from demographic_data_analyzer import load_data, analyze_data

class TestDemographicDataAnalyzer(unittest.TestCase):

    def setUp(self):
        self.data = load_data()

    def test_analyze_data(self):
        results = analyze_data(self.data)
        self.assertIsNotNone(results['race_counts'])
        self.assertIsInstance(results['average_age_men'], float)
        self.assertIsInstance(results['percentage_bachelors'], float)

if __name__ == '__main__':
    unittest.main()
