#!/usr/bin/python3
"""List all cities of a given state from the hbtn_0e_4_usa database."""

import sys
import MySQLdb


if __name__ == "__main__":

    state_name = sys.argv[4]
    query = """
    SELECT cities.id, cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name %(state_name)s
    ORDER BY cities.id ASC
    """
    trans = (state_name,)

    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        host="localhost",
        port=3306,
        db=sys.argv[3]
        )
    cursor = db.cursor()

    cursor.execute(query, trans)
    cities = cursor.fetchall()

    for city in cities:
        print("{}: {}".format(city[0], city[1]))

    cursor.close()
    db.close()
