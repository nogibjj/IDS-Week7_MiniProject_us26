"""
Reading data from a database
"""

import sqlite3


def read(database_name):
    cnt = sqlite3.connect(database_name)

    # "Name of university in USA :"

    cursor = cnt.execute(
        """SELECT "Name of University" FROM universities WHERE
                        "Location" == "United States";"""
    )

    result1 = cursor.fetchall()
    print("")  # Print new line

    # "Name of University where No of student per staff is less than 40.0"

    cursor = cnt.execute(
        """SELECT "Name of University", "No of student per staff" FROM
    universities WHERE "No of student per staff" > 40.0;"""
    )
    result2 = cursor.fetchall()

    print("")

    cursor = cnt.execute(
        """SELECT "Name of University", "No of student per staff" FROM
universities WHERE ("No of student per staff" < 40.0) AND ("Location" == "Canada");"""
    )
    result3 = cursor.fetchall()
    cnt.commit()

    return result1, result2, result3
