from main import   complex_query
import sqlite3

def test_create_table():
    main.create_table()

def test_insert_data():
    main.insert_data("John", 25)
    main.insert_data("Alice", 30)

def test_read_data():
    user_data = main.read_data()
    print("All Users:")
    for user in user_data:
        print(user)
def test_complex_query():
        results = complex_query(test.db)


        

def test_custom_queries():
    custom_connection = sqlite3.connect('test.db')
    custom_cursor = custom_connection.cursor()
    query1 = "SELECT name FROM users WHERE age > 25"
    query2 = "SELECT AVG(age) FROM users"
    
    result1 = custom_cursor.execute(query1).fetchall()
    result2 = custom_cursor.execute(query2).fetchall()

    custom_connection.close()

    print("\nUsers older than 25:")
    for user in result1:
        print(user[0])

    print("\nAverage age of all users:")
    for avg_age in result2:
        print(avg_age[0])
