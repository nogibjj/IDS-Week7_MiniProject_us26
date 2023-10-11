"""
deletion of data present in the table.
"""
import sqlite3
from datetime import datetime


def delete(Database_Name):
    con = sqlite3.connect(Database_Name)
    con.execute("""DELETE FROM universities WHERE "Industry Income Score" < 90.0;""")

    cursor = con.execute("""SELECT "Name of University" FROM universities""")
    con.commit()

    results = cursor.fetchall()
    return results


def report():
    result = {"Successfully completed CRUD operation"}
    return result


def create_summary(file_path):
    now = datetime.now()
    dt_string = now.strftime("%d-%b-%Y %H:%M") + " (UTC)"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(dt_string)
        f.write("\n")
        f.write(str(report()))
