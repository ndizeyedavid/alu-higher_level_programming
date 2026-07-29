#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa."""
import sys
import MySQLdb


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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
