#!/usr/bin/python3
"""This script lists all cities from the hbtn_0e_4_usa database."""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
            JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
