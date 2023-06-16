#!/usr/bin/python3

"""imports a module."""


import MySQLdb
from sys import argv

if __name__ == 'main':
    """main."""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], password=argv[2],
                           db=argv[3],  state_name_searched = sys.argv[4], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == state_name_searched:
            print(row)

    cur.close()
    db.close()
