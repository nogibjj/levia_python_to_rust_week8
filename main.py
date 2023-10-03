# main.py

import sqlite3

def create_table():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")
    connection.commit()
    connection.close()

def insert_data(name, age):
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Jess", 30))
    connection.commit()
    connection.close()

def read_data():
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM users')
    data = result.fetchall()
    connection.close()
    return data
