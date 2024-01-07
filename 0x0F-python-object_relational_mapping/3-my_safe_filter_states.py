#!/usr/bin/python3
"""
This script is safe from MySQL injections. It displays all values in the 
states table of hbtn_0e_0_usa where the name matches the provided argument.
It accepts four arguments: MySQL username, MySQL password, database name,
and state name.
"""

import MySQLdb
import sys


def search_state_safe(username, password, db_name, state_name):
    """
    Displays all values in the states table where name matches the state_name,
    safe from MySQL injections.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        search_state_safe(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
