# SP500-Data-Filter
This Python project processes historical S&P 500 market data from a CSV file. Each row is parsed into structured objects, filtered by closing price, and the results can be displayed as a formatted table in the console or stored in a SQLite database, where the program creates the database and tables, inserts the original data, and generates a filtered table.

> **Note:** This project was created for academic and learning purposes. It is not intended for production use.

## Installation

1. Ensure **Python 3.12** is installed on your system.
2. Download or clone the repository and navigate to the project directory.
3. No external dependencies are required — the project uses only Python standard libraries (`csv`, `sqlite3`, `unittest`, and `io`).

## Usage

Make sure the dataset file (`sp500_data.csv`) is located in the project folder, then run the program using the main Python file.

You will be prompted with the following menu:

```
S&P 500 Data Filter
--------------------
1 - Print filtered CSV data
2 - Create SQL tables and insert data
3 - Exit
```

## Key Functionality

- **Option 1 – Data Filtering (Console Output)**
  - Reads CSV data
  - Filters rows where `close > 6800`
  - Displays formatted results in a table

- **Option 2 – Database Creation & Storage**
  - Creates a SQLite database: `sp500_database.db`
  - Builds two tables:
    - `original_data` (raw dataset)
    - `filtered_data` (filtered subset)
  - Inserts and filters data using SQL queries

## Features

- CSV parsing with handling for empty rows  
- Object-oriented design using `SP500Entry`  
- Filtering based on financial thresholds  
- SQLite database integration  
- Automated table creation and data insertion  
- Formatted console output
- Unit testing 

## Project Structure

```
SP500-Data-Filter/
├── main.py
├── sp500_data.csv
├── sp500_data_class.py
├── test_database.py
├── test_data_processing.py
└── sp500_database.db (generated at runtime)
```

## Skills Demonstrated

- Python programming  
- File handling and CSV parsing  
- Database management with SQLite  
- SQL queries and data transformation
- Implementation of unit tests 

## Future Improvements
 
- Add data visualization (matplotlib)

## License

[MIT](https://choosealicense.com/licenses/mit/)
