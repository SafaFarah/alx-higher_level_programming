#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists all 
cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id=states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    row = cur.fetchall()
    city = ", ".join(i[0] for i in row)
    print(city)
    cur.close()
    db.close()
