#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""


from sys import argv
import MySQLdb
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], database=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id""".format(argv[4]))
    row = cur.fetchall()
    for i in row:
        print(i)
    cur.close()
    db.close()
