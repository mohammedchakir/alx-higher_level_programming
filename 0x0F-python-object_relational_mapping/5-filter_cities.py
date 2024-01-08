#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
It takes four arguments: MySQL username, MySQL password, database name,
and state name.
The script is safe from SQL injection.
"""

import MySQLdb
import sys


def list_cities_of_state(username, password, db_name, state_name):
    """
    Lists all cities of a given state in ascending order by cities.id.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    query = "SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_cities_of_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
