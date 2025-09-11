#!/usr/bin/python3
"""A script to query a MySQL database for states starting with 'N'.

This script connects to a MySQL database using the provided credentials
and database name, and prints all states where the name starts with 'N'
(upper N), sorted by id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
