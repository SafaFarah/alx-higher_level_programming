#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. write one that is
safe from MySQL injections!
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id",
                (argv[4], ))
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
