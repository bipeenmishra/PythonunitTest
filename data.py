import unittest
from statistics import mean
import numpy
import pandas as pd
csv = 'demo_data_churn.csv'

df2 = pd.read_csv(csv)
su = df2['gross_sales'].sum()
x = 2719153786.144917


class TestingSum(unittest.TestCase):

    def test_negative(self):
        firstValue = su
        secondValue = 0
        message ="Total sales:",su

        self.assertEqual(firstValue, secondValue, message)

if __name__ == '__main__':
    unittest.main()