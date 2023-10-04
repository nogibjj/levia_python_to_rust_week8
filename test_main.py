import pytest
import main

@pytest.fixture
def setup_database():
    main.create_table()
    yield
    connection = main.sqlite3.connect('testpy.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE users')
    connection.commit()
    connection.close()

def test_insert_and_read_data(setup_database):
    main.insert_data("John", 25)
    data = main.read_data()
    assert len(data) == 1
    assert data[0][1] == "John"
    assert data[0][2] == 25

def test_insert_multiple_data(setup_database):
    main.insert_data("Alice", 30)
    main.insert_data("Bob", 35)
    data = main.read_data()
    assert len(data) == 2

def test_custom_query(setup_database):
    main.insert_data("Alice", 30)
    main.insert_data("Bob", 35)

    query = "SELECT name FROM users WHERE age > 30"
    result = main.custom_query(query)
    assert len(result) == 1
    assert result[0][0] == "Bob"

if __name__ == '__main__':
    pytest.main()
