#!/usr/bin/python3
"""Acess database tables
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """List all cities with under state
    given as argument
    """

    try:
        cnx = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                charset='utf8'
                )
        cursor = cnx.cursor()
        query = """SELECT * FROM cities
        INNER JOIN states ON cities.state_id = states.id
        ORDER BY cities.id"""
        cursor.execute(query)
        rows = cursor.fetchall()
        print(', '.join(r[2] for r in rows if r[4] == sys.argv[4]))
    except MySQLdb.Error as err:
        print("MySQLdb error:", err)
    finally:
        if cnx:
            cnx.close()
        
