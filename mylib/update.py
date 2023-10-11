"""
Updating of tuple values already present in the table
"""
import sqlite3


def update(Database_Name):
    con = sqlite3.connect(Database_Name)

    con.execute(
        """UPDATE universities SET "Location" = 'not found' WHERE
    "Location" IS NULL;"""
    )

    cursor = con.execute("""SELECT * FROM universities""")

    results = cursor.fetchall()
    con.commit()
    return results
