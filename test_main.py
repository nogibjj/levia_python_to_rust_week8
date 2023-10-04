import main
import sqlite3
import pytest

@pytest.fixture
def setup_database():
    main.create_table()
    yield
    connection = sqlite3.connect('test.db')
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
