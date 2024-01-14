#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa using argv:
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    try:
        cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY states.id", argv[4])
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception:
        pass
