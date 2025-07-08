from sqlite3 import connect

con = connect("db.sqlite3")

cu = con.cursor()
CREATE_TABLE_COMMAND = """ 
CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    username TEXT,
    fullname TEXT,
    CONSTRAINT username_constraint UNIQUE (username)
)
"""
DELETE_COMMAND = """
DROP TABLE student
"""
CREATE_COMMAND = """
INSERT INTO student (username, fullname)
VALUES (?, ?)
"""
# cu.execute(CREATE_TABLE_COMMAND)
cu.execute(CREATE_COMMAND, ("sasha2", "Александр"))
con.commit()
