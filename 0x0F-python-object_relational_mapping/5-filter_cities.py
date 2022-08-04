#!/usr/bin/python3
""" List all state in database """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    qstate = argv[4]
    result = ""
    separator = ""

    conn = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=argv[1],
      passwd=argv[2],
      db=argv[3])

    cur = conn.cursor()
    cur.execute('''
        SELECT cities.name, cities.id, states.name
        FROM cities INNER JOIN states
        WHERE cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')

    query_rows = cur.fetchall()

    for row in query_rows:
        if (qstate == row[2]):
            result += separator
            result += row[0]
            separator = ', '
    print(result)

    cur.close()
    conn.close()
