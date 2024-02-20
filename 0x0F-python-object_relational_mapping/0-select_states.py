#!/usr/bin/python3
""" This module contains code to connect to a database
"""
import MySQLdb
import sys

if '__name__' == '__main__':
    """List all states from database 'tbtn_0e_0_usa'
    """

    cnx = MySQLdb.connect(
            host=localhost,
            port=3306,
            user=sys.argv[1],
            user=sys.argv[2],
            db=sys.argv[3]
    )
    cursor = cnx.cursor()
    query = "SELECT * FROM states"
    cursor.execute(query)
    [print(state) for state in cursor.fetchall()]
