#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Connect to the database, retrieve data and display
    it if a valid state is given as an argument.
    Otherwise, print an error message.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id".format(sys.argv[4])

    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
