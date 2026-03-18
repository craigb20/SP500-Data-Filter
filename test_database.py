import unittest
import sqlite3
from main import create_tables


class TestDatabaseSetup(unittest.TestCase):

    def test_tables_created(self):
        create_tables()

        conn = sqlite3.connect('sp500_database.db')
        cursor = conn.cursor()

        # Check if tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in cursor.fetchall()}

        self.assertIn("original_data", tables)
        self.assertIn("filtered_data", tables)

        conn.close()


if __name__ == "__main__":
    unittest.main()
