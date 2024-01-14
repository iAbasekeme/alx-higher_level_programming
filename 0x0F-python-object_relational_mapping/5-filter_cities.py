#!/usr/bin/python3
"""
A script that lists all cities from
the database hbtn_0e_0_usa using argv
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    state_name = argv[4]
    db = MySQLdb.connect(
        host='localhost', user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    try:
        cur.execute("SELECT cities.name FROM cities \
            INNER JOIN states ON states.id = cities.state_id WHERE states.name = %s", (state_name,))
        rows = cur.fetchall()
        list_cities = []
        for row in rows:
            list_cities.append(row[0])
        print(", ".join(list_cities))
        cur.close()
        db.close()
    except Exception:
        pass
