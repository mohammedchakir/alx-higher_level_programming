#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
It takes three arguments: MySQL username, MySQL password, and database name.
"""

import MySQLdb
import sys


def list_cities(username, password, db_name):
    """
    Lists all cities from the database in ascending order by cities.id.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
