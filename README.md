## Python script into a command-line tool


<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/schema.png" alt="schema">
</p>


### Overview

Using the sqlite-utils command-line tool we can directly run the sql commands from cmd. It can be used to manipulate SQLite databases in a number of different ways. I will again be doing CRUD operations but directly from terminal.

### User Guide

This is the **default subcommand**, so the following two examples work the same way:

	sqlite-utils query dogs.db "select * from dogs"

	sqlite-utils dogs.db "select * from dogs"

**UPDATE, INSERT and DELETE**

If you execute an UPDATE, INSERT or DELETE query the command will return the number of affected rows:

    sqlite-utils dogs.db "update dogs set age = 5 where name = 'Cleo'"

    [{"rows_affected": 1}]

If your data is in **CSV format**, you can insert it using the --csv option:

    sqlite-utils insert dogs.db dogs dogs.csv --csv

Here is the documentation for more command line tools for reference [sqlite-utils](https://sqlite-utils.datasette.io/en/stable/cli.html)


### Code Description

This repo has been created by forked from (https://github.com/nogibjj/sqlite-lab). I have used world university ranking csv file and loaded it into 'ranking.db' database under the table name 'universities'. 

1. create.py
    This script is used for load and transform. A databased called 'ranking.db' with a table named 'universities' is created and a csv file is loaded into that table.

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/create.png" alt="schema">
</p>

2. read.py
    This script is used to interact with the SQL database. The queries used are :
    - sqlite-utils query ranking.db 'SELECT "Name of University" FROM universities WHERE
      "Location" == "United States"'
    - sqlite-utils query ranking.db 'SELECT "Name of University", "No of student per staff" FROM
      universities WHERE "No of student per staff" > 40.0'
    - sqlite-utils query ranking.db 'SELECT "Name of University", "No of student per staff" FROM
        universities WHERE ("No of student per staff" < 40.0) AND ("Location" == "Canada")'

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/read.png" alt="schema">
</p>

3. update.py
    Updating of tuple values already present in the table.

    - sqlite-utils query ranking.db "update universities set Location = 'australia' where Location = 'Australia'"

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/update.png" alt="schema">
</p>

4. delete.py
    Deletion of data present in the table. The query used is :
      sqlite-utils query ranking.db 'DELETE FROM universities WHERE "Industry Income Score" < 90.0'

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/delete.png" alt="schema">
</p>

6. test_graph.py
    ** pd.read_sql_query **  is used for creating visualisation.
    It is a function used to read SQL query or database table into DataFrame.
   
6. Makefile with the following:

	- install: using requirements.txt file to install required packages

	- test:

	python -m pytest -vv --cov=main *.py
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/test.png" alt="install">
</p>

	- format: using black formatter

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/format.png" alt="format">
</p>

      - lint: using ruff 

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/lint.png" alt="lint">
</p>	

7.Created GitHub Actions that performs all four Makefile commands with badges for each one in the README.md

##### Action include the general CI/CD process in test.yml file, which automatically generate the graph and markdown

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS-Week5_MiniProject_us26/blob/main/images/ci_cd.png" alt="cicd">
</p>

## Visualization 
#### Visualization Created using sql database using pandas.read_sql_query (https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html)

##### Count of top universities vs mean industry income score 

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/output_graph/visualization.png" alt="visualization">
</p>	
