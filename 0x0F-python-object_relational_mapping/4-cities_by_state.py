#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    import MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states ON\
                   cities.state_id = states.id\
                   ORDER BY cities.id")
    result = cursor.fetchall()
    for city in result:
        print(city)
