# SQLite Database Operations

This Python script demonstrates basic database operations using SQLite. SQLite is a lightweight and self-contained database engine, and this script shows you how to create a database, create a table, insert data, read data, and execute custom SQL queries.

## Code Explanation

### Database Creation

Create a SQLite database named `test.db`. 

```python
create_table()
```

This function creates a table named `users` with columns `id` (integer, primary key), `name` (text), and `age` (integer).

### Inserting Data

Insert data into the `users` table using the `insert_data` function. You can insert additional data by calling this function with the desired `name` and `age` values.

```python
insert_data("John", 25)
insert_data("Alice", 30)
```

### Reading Data

To retrieve data from the `users` table, the `read_data` function is used. This function fetches all rows from the table and returns them as a list of tuples.

```python
user_data = read_data()
```

### Custom Queries

1. Select names of users older than 25:

```python
query1 = "SELECT name FROM users WHERE age > 25"
```

2. Calculate the average age of all users:

```python
query2 = "SELECT AVG(age) FROM users"
```

These queries are executed using a custom connection and cursor, and the results are printed to the console.

```python
result1 = custom_cursor.execute(query1).fetchall()
result2 = custom_cursor.execute(query2).fetchall()
```

## Execution

  <img width="355" alt="Screenshot 2023-10-04 at 12 07 12 AM" src="https://github.com/nogibjj/levia_sql_connection_week5/assets/73449544/27005c8c-cf2d-4805-9f82-5d2fc324fd41">

