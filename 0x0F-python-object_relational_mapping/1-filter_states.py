#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
with a name starting with N (upper N).
It takes three arguments: MySQL username, MySQL password, and database name.
"""

import MySQLdb
import sys

def list_states_with_n(username, password, db_name):
    """
    Lists all states with names starting with 'N' from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
