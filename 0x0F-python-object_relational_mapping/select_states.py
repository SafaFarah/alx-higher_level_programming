#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb
db = MySQLdb.connect(host="localhost", user=argv[1],
                     database=argv[2], port=3306)
cur = db.cursor()
cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id""".format(argv[3]))
row = cur.fetchall()
for i in row:
    print(i)
cur.close()
db.close()
