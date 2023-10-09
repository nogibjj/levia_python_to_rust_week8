# SQLite Database Operations

This Python script demonstrates basic database operations using SQLite. SQLite is a lightweight and self-contained database engine, and this script shows you how to create a database, create a table, insert data, read data, and execute custom SQL queries.

## Code Explanation

### Database Creation

Create a SQLite database named `test.db`. 

```python
create_table()
```

## Joining Tables

```sql
SELECT u.name, o.order_date
FROM users u
INNER JOIN orders o ON u.id = o.user_id
WHERE u.age > 25
ORDER BY o.order_date DESC;
```

**Explanation:**

- This query retrieves data from two tables: `users` (aliased as `u`) and `orders` (aliased as `o`).
- It performs an inner join between the two tables based on the `user_id` in the `orders` table matching the `id` in the `users` table.
- The `WHERE` clause filters the results to include only users with an age greater than 25.
- Finally, the `ORDER BY` clause sorts the results by the `order_date` column in descending order.


## Complex SQL Query Example 2: Aggregation

```sql
SELECT u.name, AVG(o.total_amount) AS avg_order_amount
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.name
HAVING AVG(o.total_amount) > 100;
```

**Explanation:**

- This query also retrieves data from the `users` and `orders` tables, performing an inner join.
- It uses the `GROUP BY` clause to group the results by the user's name (`u.name`).
- Within each group, it calculates the average (`AVG`) of the `total_amount` column from the `orders` table and aliases it as `avg_order_amount`.
- The `HAVING` clause filters the groups to include only those where the average order amount is greater than 100.


## Execution

