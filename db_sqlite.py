import sqlite3
import json

DB_FILE = "measurements.db"


def insert_measurement(input_values):
    """ Insert values into the database and fetch the latest entry """
    try:
        # Create a database connection
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Create table if it doesn't exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS measurements (
                            nitrogen INTEGER,
                            phosphorus INTEGER,
                            potassium INTEGER,
                            temperature INTEGER,
                            humidity INTEGER,
                            moisture INTEGER
                          );''')

        # Insert new values
        cursor.execute('''INSERT INTO measurements 
                          (nitrogen, phosphorus, potassium, temperature, humidity, moisture) 
                          VALUES (?, ?, ?, ?, ?, ?)''', input_values)
        conn.commit()

        # Fetch the latest entry
        cursor.execute(
            "SELECT * FROM measurements ORDER BY rowid DESC LIMIT 1;")
        row = cursor.fetchone()

        # Close the connection
        conn.close()

        # Process and return the result
        if row:
            column_names = ['nitrogen', 'phosphorus',
                            'potassium', 'temperature', 'humidity', 'moisture']
            data = dict(zip(column_names, row))
            return json.dumps(data, indent=4)
        else:
            return json.dumps({})

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

        # Fetch the latest entry
        cursor.execute(
            "SELECT * FROM measurements ORDER BY rowid DESC LIMIT 1;")
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
