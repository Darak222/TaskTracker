import sqlite3 as sl

connect = sl.connect('testbase.db')

sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]

with connect:
    #data = connect.execute("SELECT * FROM USER WHERE age <= 22")
    #for row in data:
    #    print(row)

    names = connect.execute("Select * FROM CHARACTERS")
    for name in names:
        print(name)

    #tables = connect.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #for table in tables:
    #    print(table)
