import sqlite3
import pandas as pd
from config import DB_FILE, TABLE_NAME, CSV_FILE

def create_database():
    """Creates the database and populates it with data from a CSV file."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Drop the table if it exists
        cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")

        # Read the CSV data into a pandas DataFrame
        df = pd.read_csv(CSV_FILE)

        # Create the table from the DataFrame
        df.to_sql(TABLE_NAME, conn, index=False, if_exists='replace')

        print(f"Database '{DB_FILE}' created successfully.")
        print(f"Table '{TABLE_NAME}' created and populated with {len(df)} rows.")

        conn.commit()
        conn.close()

    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_database()
