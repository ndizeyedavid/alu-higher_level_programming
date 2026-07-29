#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists
all cities of that state from the database hbtn_0e_4_usa."""
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cur.close()
    db.close()
