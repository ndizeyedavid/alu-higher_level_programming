#!/usr/bin/python3
"""Script that takes an argument and displays all values in the states
table where name matches the argument (safe from SQL injection)."""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
