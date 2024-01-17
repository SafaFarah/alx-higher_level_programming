#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id=states.id ORDER BY cities.id")
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
