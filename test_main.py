# # test_main.py

# import unittest
# import main  # Import the main.py file
# import sqlite3

# class TestMain(unittest.TestCase):

#     def setUp(self):
#         main.create_table()  # Create the table before each test

#     def test_insert_and_read_data(self):
#         main.insert_data("John", 25)
#         data = main.read_data()
#         self.assertEqual(len(data), 1)
#         self.assertEqual(data[0][1], "John")
#         self.assertEqual(data[0][2], 25)

#     def test_insert_multiple_data(self):
#         main.insert_data("Alice", 30)
#         main.insert_data("Bob", 35)
#         data = main.read_data()
#         self.assertEqual(len(data), 2)

#     def tearDown(self):
#         # Clean up the database after each test
#         connection = sqlite3.connect('test.db')
#         cursor = connection.cursor()
#         cursor.execute('DROP TABLE users')
#         connection.commit()
#         connection.close()

# if __name__ == '__main__':
#     unittest.main()
