#!/usr/bin/python3
"""Access database using MySQLdb
ensure no SQL injection vulnerabilities
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """List all rows of database table
    eliminate SQL injection vulnerabilities
    """

    cnx = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = cnx.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s"
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cnx.close()
