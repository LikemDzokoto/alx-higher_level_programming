#!/usr/bin/python3
''' return only matching states, safe from MYSQL injections '''

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    search = sys.argv[4]
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        if search == state[1]:
            print(state)
