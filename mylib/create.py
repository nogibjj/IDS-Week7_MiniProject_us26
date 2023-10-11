"""
Creating a database and importing a csv file into table
"""

import sqlite3
import pandas as pd


def create(Database_Name):
    con = sqlite3.connect(Database_Name)
    df = pd.read_csv("World University Rankings 2023.csv")

    df.to_sql("universities", con, if_exists="replace", index=False)

    # cursor = con.execute("SELECT * FROM universities")
    # result = cursor.fetchall()
    con.commit()
    con.close()

    return "Database with table named universities created"
