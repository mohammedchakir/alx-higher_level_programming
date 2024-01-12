#!/usr/bin/python3
"""This script lists all cities of a specified state
from the hbtn_0e_4_usa database."""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3],
        )
    cursor = db.cursor()

    query = ("SELECT cities.id, cities.name FROM cities JOIN states \
            ON cities.state_id = states.id WHERE states.name \
            LIKE BINARY %(state_name)s ORDER BY cities.id ASC", (sys.argv[4],))

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
