#!/usr/bin/python3
"""Access tables in database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """List all cities in database
    """
    cnx = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = cnx.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
