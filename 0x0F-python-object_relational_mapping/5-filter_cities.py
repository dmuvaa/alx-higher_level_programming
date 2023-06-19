#!/usr/bin/python3

"""imports a module"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """main"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2],
                           db=argv[3], charset="utf8")

    cur = conn.cursor()

    state_name = argv[4]

    cur.execute("SELECT cities.id, cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (state_name,))

    rows = cur.fetchall()

    print(", ".join(row[1] for row in rows))

    cur.close()
    conn.close()
