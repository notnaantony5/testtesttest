from sqlite3 import connect

con = connect("db.sqlite3")

cu = con.cursor()
COMMAND = """ 
CREATE TABLE test(
    id INT PRIMARY KEY
)
"""
cu.execute(COMMAND)
