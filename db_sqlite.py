import sqlite3
import json
from datetime import datetime, timedelta

DB_FILE = "measurements.db"


def insert_measurement(input_values, time_limit=True):
    """ Insert values into the database with a timestamp. 
        Only insert if it's been at least 6 hours since the last entry. """
    try:
        # Create a database connection
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create table if it doesn't exist with an additional time_modified column
        cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                            nitrogen INTEGER,
                            phosphorus INTEGER,
                            potassium INTEGER,
                            temperature INTEGER,
                            humidity INTEGER,
                            moisture INTEGER,
                            time_modified TEXT
                          );''')

        # Check the time of the last entry
        cursor.execute(
            "SELECT time_modified FROM measurements ORDER BY rowid DESC LIMIT 1;")
        last_entry = cursor.fetchone()

        if time_limit and last_entry:
            last_time = datetime.strptime(
                last_entry[0], '%Y-%m-%dT%H:%M:%S.%fZ')
            if datetime.utcnow() - last_time < timedelta(hours=6):
                return False

        # Insert new values with current UTC timestamp
        cursor.execute('''INSERT INTO measurements 
                          (nitrogen, phosphorus, potassium, temperature, humidity, moisture, time_modified) 
                          VALUES (?, ?, ?, ?, ?, ?, strftime('%Y-%m-%dT%H:%M:%fZ', 'now'))''', input_values)
        conn.commit()

        # Close the connection
        conn.close()
        return True

    except sqlite3.Error as e:
        print(e)
        return None


def read_latest_entry_as_json():
    """ Fetch the latest entry from the database and return it as a list of dicts 
    such as [{"N": 10}, {"P": 11}, {"K": 12}, {"T": 5}, {"H": 6}, {"M": 7}] """
    try:
        # Create a database connection
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch the latest entry excluding the time_modified column
        cursor.execute(
            "SELECT nitrogen, phosphorus, potassium, temperature, humidity, moisture FROM measurements ORDER BY rowid DESC LIMIT 1;")
        row = cursor.fetchone()

        # Close the connection
        conn.close()

        # Process and return the result
        if row:
            column_names = ['N', 'P', 'K', 'T', 'H', 'M']
            data = [{column_names[i]: row[i]} for i in range(len(row))]
            return json.dumps(data)
        else:
            return json.dumps([])

    except sqlite3.Error as e:
        print(e)
        return None
