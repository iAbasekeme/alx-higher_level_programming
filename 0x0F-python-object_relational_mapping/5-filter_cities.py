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
        query = "SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON states.id = cities.state_id WHERE states.name = %s \
            ORDER BY cities.id ASC"
        cur.execute(query, argv[4])
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except Exception:
        pass
