#!/usr/bin/python3
""" 2-my_filter_states.py

    takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def main():
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    search = sys.argv[4]

    db = MySQLdb.connect(
         "localhost",
         mysql_username,
         mysql_password,
         database_name,
         3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name={} LIKE BINARY 'N%' \
                    ORDER BY states.id ASC".format(search))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()