#!/usr/bin/python3
"""Connect to mysql to list database
"""


import MySQLdb
import sys


if __name__ == '__main__':
    """Access database for a key word
    """
    cnx = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = cnx.cursor()
    query = "SELECT * FROM states \
            WHERE name = '{}'".format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
