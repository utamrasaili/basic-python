import sqlite3
# connect to database(create a new one if it doesnt exit)

conn=sqlite3.connect('mydatabase.db')

# create a cursor object to excecute SQL commands
cursor= conn.cursor()

# define table structure
cursor.execute('''CREATE TABLE IF NOT EXISTS user(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
age INTEGER,
email TEXT UNIQUE
)
''')

# # insert a single record
# cursor.execute("INSERT INTO user(username,age,email)VALUES('alice',30,'alice@example.com')") [using without taking from user ]

# name=input("enter the name")
# age=int(input("enter the age"))
# email=input("enter the email")
# cursor.execute('INSERT INTO user (username,age,email)VALUES(?,?,?)',(name,age, email))


# users=[
#     ('bob',25,'bob@example.com'),
#     ('charlie',35,'charlie@example.com')
# ]
# cursor.executemany("INSERT INTO user(username,age,email)VALUES(?,?,?)",users)

conn.commit()

# cursor.execute("SELECT * FROM user")
# rows= cursor.fetchall()
# print(rows)
