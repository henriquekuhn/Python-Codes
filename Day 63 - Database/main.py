import sqlite3
import os

DIR = os.getcwd() + "/Day 63 - Database"
os.chdir(DIR)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()