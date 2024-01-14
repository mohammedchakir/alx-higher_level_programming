#!/usr/bin/python3
"""List all cities of a given state from the hbtn_0e_4_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":

   db = MySQLdb.connect(
       host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
   
   cursor = db.cursor()
   query = """SELECT cities.name
                   FROM cities
                   INNER JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id"""
   
   cursor.execute(query, (sys.argv[4],))
   
   cities = cursor.fetchall()
   parms = list(city[0] for city in cities)
   print(*parms, sep=", ")
   
   cursor.close()
   db.close()

