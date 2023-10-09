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

def complex_query(db_name='test.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Joining tables
    query1 = """
    SELECT u.name, o.order_date
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    WHERE u.age > 25
    ORDER BY o.order_date DESC;
    """
    result1 = cursor.execute(query1).fetchall()

    # Aggregation
    query2 = """
    SELECT u.name, AVG(o.total_amount) AS avg_order_amount
    FROM users u
    INNER JOIN orders o ON u.id = o.user_id
    GROUP BY u.name
    HAVING AVG(o.total_amount) > 100;
    """
    result2 = cursor.execute(query2).fetchall()

    connection.close()
    return result1, result2

if __name__ == '__main__':
    # Create the table
    create_table()

    # Insert data
    insert_data("John", 25)
    insert_data("Alice", 30)
    insert_data("Bob", 22)
    insert_data("Ana", 35)
    insert_data("Jake", 28)


    # Read data
    user_data = read_data()
    print("All Users:")
    for user in user_data:
        print(user)

    # # Execute custom queries
    # custom_connection = sqlite3.connect('test.db')
    # custom_cursor = custom_connection.cursor()
    # query1 = "SELECT name FROM users WHERE age > 25"
    # query2 = "SELECT AVG(age) FROM users"
    
    # result1 = custom_cursor.execute(query1).fetchall()
    # result2 = custom_cursor.execute(query2).fetchall()


    # Execute complex queries
    results = complex_query()
    
    print("\nComplex Query 1: Users older than 25 with their recent orders:")
    for row in results[0]:
        print(row)

    print("\nComplex Query 2: Users with average order amount over 100:")
    for row in results[1]:
        print(row)
        
    custom_connection.close()
