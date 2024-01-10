#!/usr/bin/python3
"""
A script that displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

def search_state(username, password, db_name, state_name):
    """
    Connects to a MySQL database and prints states
    where name matches the given argument.
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name)
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
        search_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
