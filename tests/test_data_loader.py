import unittest
import pandas as pd
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        df = load_data("sample.csv")
        self.assertIsInstance(df, pd.DataFrame)


if __name__ == "__main__":
    unittest.main()