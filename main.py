import sqlite3

def create_table(db_name='test.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")
    connection.commit()
    connection.close()

def insert_data(name, age, db_name='test.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    connection.commit()
    connection.close()

def read_data(db_name='test.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    result = cursor.execute('SELECT * FROM users')
    data = result.fetchall()
    connection.close()
    return data

if __name__ == '__main__':
    # Create the table
    create_table()

    # Insert some data
    insert_data("John", 25)
    insert_data("Alice", 30)

    # Read data
    data = read_data()
    print("All Users:")
    for user in data:
        print(user)

    # Execute custom queries
    connection = sqlite3.connect('test.db')
    cursor = connection.cursor()
    query1 = "SELECT name FROM users WHERE age > 25"
    query2 = "SELECT AVG(age) FROM users"
    
    result1 = cursor.execute(query1).fetchall()
    result2 = cursor.execute(query2).fetchall()

    connection.close()

    print("\nUsers older than 25:")
    for user in result1:
        print(user[0])

    print("\nAverage age of all users:")
    for avg_age in result2:
        print(avg_age[0])
