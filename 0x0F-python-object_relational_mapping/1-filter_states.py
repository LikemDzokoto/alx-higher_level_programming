#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE
                   BINARY 'N%' ORDER BY id ASC""")
    results = cursor.fetchall()

    for row in results:
        print(row)
