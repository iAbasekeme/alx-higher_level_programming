#!/usr/bin/python3
"""
A script that lists all cities from
the database hbtn_0e_0_usa using argv
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    try:
        query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id"
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception:
        pass
