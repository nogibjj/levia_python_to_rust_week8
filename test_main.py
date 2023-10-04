import main
import pytest

@pytest.fixture
def setup_database():
    main.create_table()
    yield
    connection = main.sqlite3.connect('test.db')
    cursor = connection.cursor()
    cursor.execute('DROP TABLE users')
    connection.commit()
    connection.close()

def test_insert_data(setup_database):
    main.insert_data("Alice", 30)

def test_read_data(setup_database):
    data = main.read_data()
    # You can add assertions here to validate the data if needed

def test_custom_query(setup_database):
    query = "SELECT name FROM users WHERE age > 25"
    result = main.custom_query(query)
    # You can add assertions here to validate the result if needed
