#!/usr/bin/python3
""" List all state in database """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    username = argv[1]
    upasswd = argv[2]
    sqldb = argv[3]

    conn = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=username,
      passwd=upasswd,
      db=sqldb)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()

