#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa
"""




if __name__ == "__main__":
    import MySQLdb
    import sys
    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # create cursor to exec queries using SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    
