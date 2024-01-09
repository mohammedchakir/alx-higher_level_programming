#!/usr/bin/python3
"""
A script that lists all states with names starting with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states_starting_with_n(username, password, db_name):
    """
    Connects to a MySQL database and prints all states starting
    with 'N', sorted by id.
    """
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_starting_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
