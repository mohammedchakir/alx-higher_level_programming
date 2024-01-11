#!/usr/bin/python3
"""This script retrieves data from the states table
based on the provided state name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connect to the database and retrieve information
    about a specific state.
    """
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    results = cursor.fetchall()
    
    for row in results:
        print(row)
    cursor.close()
    db.close()
