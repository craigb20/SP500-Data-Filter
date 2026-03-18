import unittest
from io import StringIO
from main import create_data_table


class TestCSV(unittest.TestCase):

    def test_create_data_table(self):
        # Test CSV data
        test_file = StringIO("""Date,Open,High,Low,Close
3/12/2026,6740.88,6740.88,6670.4,6672.62
3/11/2026,6790.09,6811.15,6745.59,7000
""")

        # Run the function
        result = create_data_table(test_file)

        # Check it runs without errors
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
