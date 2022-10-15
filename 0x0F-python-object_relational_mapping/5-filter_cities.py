#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    search = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities\
                   JOIN states ON cities.state_id = states.id WHERE\
                   states.name = %(search)s", {'search': search})

    result = []

    for city in cursor.fetchall():
        result.extend(city)
    print(", ".join(result))
