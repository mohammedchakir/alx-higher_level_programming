#!/usr/bin/python3
"""List all cities of a given state from the hbtn_0e_4_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command-line arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    try:
        # Create a connection to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Format the SQL query to retrieve cities of the given state
        query = """SELECT cities.id, cities.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id"""

        cursor.execute(query, (state_name,))

        # Fetch and display the results
        cities = cursor.fetchall()
        for city in cities:
            print("{}: {}".format(city[0], city[1]))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()

