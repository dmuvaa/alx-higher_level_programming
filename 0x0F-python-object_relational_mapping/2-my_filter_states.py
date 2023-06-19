#!/usr/bin/python3

"""imports a module."""


import MySQLdb
from sys import argv

if __name__ == 'main':
    """main."""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
