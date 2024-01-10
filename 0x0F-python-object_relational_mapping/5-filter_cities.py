#!/usr/bin/python3
import MySQLdb
import sys

def list_cities(username, password, dbname, state_name):
    """
    This function connects to the MySQL database and lists all cities
    of a given state in an ascending order by cities.id.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    cur = db.cursor()
    
    # Use parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row[0])

    cur.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        list_cities(username, password, dbname, state_name)
    else:
        print("Usage: ./script.py mysql_username mysql_password database_name state_name")
