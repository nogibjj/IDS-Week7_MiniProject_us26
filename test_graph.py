import pandas as pd
import plotly.express as px
import sqlite3
import os

con = sqlite3.connect("ranking.db")


def visualization(con):
    result1 = pd.read_sql_query(
        "SELECT Location, COUNT(`University Rank`) "
        + " AS RankCount FROM universities "
        + "GROUP BY Location",
        con=con,
    )
    result2 = pd.read_sql_query(
        "SELECT Location, AVG(`Industry Income Score`)"
        + "AS Score FROM universities GROUP BY Location",
        con=con,
    )

    joined = result1.merge(result2, how="inner", on="Location")

    fig = px.scatter(
        joined,
        x=joined["Score"],
        y=joined["RankCount"],
        color=joined["Location"],
        size=joined["RankCount"],
    )

    fig.update_layout(
        title="Analysing Top Universities",
        xaxis_title="Mean of Industry Income Score",
        yaxis_title="Count of Top Universities",
    )
    # fig.show()

    if not os.path.exists("./output_graph"):
        os.mkdir("output_graph")

    fig.write_image("output_graph/visualization.png")


if __name__ == "__main__":
    visualization(con)
