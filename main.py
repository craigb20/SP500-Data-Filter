import csv
import sqlite3
from sp500_data_class import SP500Entry


def create_data_label():
    """ creates the labels for the table """
    date_label = 'DATE'
    open_label = 'OPEN'
    high_label = 'HIGH'
    low_label = 'LOW'
    close_label = 'CLOSE'
    print(f' ')
    print(f'{" ":<5}{date_label:<12}{open_label:<12}{high_label:<12}{low_label:<12}{close_label:<12}')
    print(f'=============================================================')


def create_data_table(target_file):
    """ reads and prints the data from the text file """
    count = 1
    data_list = []

    reader = csv.reader(target_file)
    next(reader)

    for row in reader:
        """ skip empty rows """
        if not row:
            continue

        data_obj = SP500Entry(*row)

        if data_obj.close_price != '' and float(data_obj.close_price) > 6800:
            print(f'{count:<5}{data_obj.date:<12}{data_obj.open_price:<12}{data_obj.high_price:<12}'
                  f'{data_obj.low_price:<12}{data_obj.close_price:<12}')
            data_list.append(data_obj)
            count += 1


def create_tables():
    """ creates the database tables """
    conn = sqlite3.connect('sp500_database.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS original_data")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS original_data (
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL
        )
    ''')

    cursor.execute("DROP TABLE IF EXISTS filtered_data")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS filtered_data (
            date TEXT,
            open REAL,
            high REAL,
            low REAL,
            close REAL
        )
    ''')

    conn.commit()
    conn.close()


def insert_data_from_csv():
    """ reads csv and inserts rows into main table """
    conn = sqlite3.connect('sp500_database.db')

    with open("sp500_data.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        # skip empty rows
        rows = []
        for row in reader:
            if not row:
                continue
            rows.append(row)

        cursor = conn.cursor()

        cursor.executemany(
            "INSERT INTO original_data (date, open, high, low, close) VALUES (?, ?, ?, ?, ?)",
            rows
        )

    conn.commit()
    conn.close()


def create_filtered_data_table():
    """ creates filtered table based on close price """
    conn = sqlite3.connect('sp500_database.db')
    cursor = conn.cursor()

    cursor.execute(""" INSERT INTO filtered_data (date, open, high, low, close) SELECT date, open, high, low, close
        FROM original_data WHERE close > 6800 """)

    conn.commit()
    conn.close()


def main():
    """ executes functions based on user selection """
    while True:
        print("\nS&P 500 Data Filter")
        print("--------------------")
        print("1 - Print filtered CSV data")
        print("2 - Create SQL tables and insert data")
        print("3 - Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            try:
                target_file = open("sp500_data.csv")
            except IOError:
                print("\nError: Unable to open sp500_data.csv.")
                return

            create_data_label()
            create_data_table(target_file)
            target_file.close()
            print("\nCSV data processed successfully.")
            break

        elif choice == "2":
            create_tables()
            insert_data_from_csv()
            create_filtered_data_table()
            print("\nSQL tables created and data inserted successfully.")
            break

        elif choice == "3":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\nInvalid selection. Please choose 1, 2, or 3.")


if __name__ == '__main__':
    main()
