# import sqlite3

# cx=sqlite3.connect('ourdatabase.db')

# cursor= cx.cursor()

# # cursor.execute('''CREATE TABLE IF NOT EXISTS user(
# # id INTEGER PRIMARY KEY AUTOINCREMENT,
# # username TEXT NOT NULL,
# # age INTEGER,
# # email TEXT UNIQUE
# # ) 
# # # ''')
# # # insert a single record
# # cursor.execute("INSERT INTO user(username,age,email)VALUES('john',40,'johndon@gmail.com')")

# name=input("enter the name")
# age =int(input("enter the age"))
# email=input("enter the email")

# cursor.execute('INSERT INTO world(username,age,email)VALUES(?,?,?)',(name,age,email))



# users=[
#      ('bob',25,'bob@example.com'),
#      ('charlie',35,'charlie@example.com'),
#      ('jack',27,'jackdawson27@gmail.com')
#  ]

# cursor.executemany("INSERT INTO user(username,age,email)VALUES(?,?,?)",users)


# cx.execute('UPDATE users SET name=?, age=?, email=? WHERE id=?', (name, age, email, id ))

# cx.commit()
 
 
# import sqlite3

# # Assuming 'cx' is your database connection object
# Example: cx = sqlite3.connect('database.db')

# # Define the variables
# name = "John Doe"  # Replace with the actual name
# age = 30           # Replace with the actual age
# email = "john.doe@example.com"  # Replace with the actual email
# id = 1             # Replace with the actual user ID

# # Execute the UPDATE query
# cx.execute('UPDATE users SET name=?, age=?, email=? WHERE id=?', (name, age, email, id))
