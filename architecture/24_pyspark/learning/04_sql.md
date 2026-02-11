# Spark SQL

> **SQL queries on DataFrames** - Use familiar SQL syntax with Spark

---

## 🎯 What is Spark SQL?

Spark SQL allows you to query DataFrames using SQL syntax instead of DataFrame API.

```python
# DataFrame API
df.filter(df.age > 30).select("name", "salary")

# SQL (same result!)
spark.sql("SELECT name, salary FROM people WHERE age > 30")
```

---

## 📋 Creating Temporary Views

Before using SQL, register DataFrame as a temporary view:

```python
# Create DataFrame
df = spark.createDataFrame([
    ("Alice", 28, 75000),
    ("Bob", 35, 85000),
    ("Charlie", 42, 95000)
], ["name", "age", "salary"])

# Register as temporary view
df.createOrReplaceTempView("employees")

# Now you can query it with SQL!
result = spark.sql("SELECT * FROM employees")
result.show()
```

**View Types**:

- `createOrReplaceTempView()` - Session-scoped (disappears when session ends)
- `createGlobalTempView()` - Application-scoped (shared across sessions)

---

## 🔍 Basic SQL Queries

### SELECT

```python
# Select all columns
spark.sql("SELECT * FROM employees").show()

# Select specific columns
spark.sql("SELECT name, salary FROM employees").show()

# Select with alias
spark.sql("SELECT name AS employee_name FROM employees").show()
```

### WHERE

```python
# Filter rows
spark.sql("SELECT * FROM employees WHERE age > 30").show()

# Multiple conditions
spark.sql("""
    SELECT * FROM employees
    WHERE age > 30 AND salary > 80000
""").show()

# String matching
spark.sql("SELECT * FROM employees WHERE name LIKE 'A%'").show()
```

### ORDER BY

```python
# Sort ascending
spark.sql("SELECT * FROM employees ORDER BY age").show()

# Sort descending
spark.sql("SELECT * FROM employees ORDER BY salary DESC").show()

# Multiple columns
spark.sql("SELECT * FROM employees ORDER BY age DESC, name ASC").show()
```

### LIMIT

```python
# Get first N rows
spark.sql("SELECT * FROM employees LIMIT 5").show()

# Top 3 highest earners
spark.sql("""
    SELECT * FROM employees
    ORDER BY salary DESC
    LIMIT 3
""").show()
```

---

## 📊 Aggregations

### GROUP BY

```python
# Count by group
spark.sql("""
    SELECT city, COUNT(*) as count
    FROM employees
    GROUP BY city
""").show()

# Multiple aggregations
spark.sql("""
    SELECT
        city,
        AVG(salary) as avg_salary,
        MAX(age) as max_age,
        COUNT(*) as count
    FROM employees
    GROUP BY city
""").show()
```

### HAVING

```python
# Filter groups
spark.sql("""
    SELECT city, AVG(salary) as avg_salary
    FROM employees
    GROUP BY city
    HAVING AVG(salary) > 75000
""").show()
```

### Aggregate Functions

```python
# Common aggregations
spark.sql("""
    SELECT
        COUNT(*) as total,
        AVG(salary) as avg_salary,
        MAX(salary) as max_salary,
        MIN(salary) as min_salary,
        SUM(salary) as total_salary
    FROM employees
""").show()
```

---

## 🔗 Joins

```python
# Create two DataFrames
employees = spark.createDataFrame([
    (1, "Alice", "Engineering"),
    (2, "Bob", "Sales"),
    (3, "Charlie", "Engineering")
], ["id", "name", "dept"])

salaries = spark.createDataFrame([
    (1, 75000),
    (2, 65000),
    (3, 95000)
], ["emp_id", "salary"])

# Register views
employees.createOrReplaceTempView("employees")
salaries.createOrReplaceTempView("salaries")

# Inner join
spark.sql("""
    SELECT e.name, e.dept, s.salary
    FROM employees e
    INNER JOIN salaries s ON e.id = s.emp_id
""").show()

# Left join
spark.sql("""
    SELECT e.name, e.dept, s.salary
    FROM employees e
    LEFT JOIN salaries s ON e.id = s.emp_id
""").show()
```

---

## 🔧 Advanced SQL Features

### CASE WHEN

```python
# Conditional logic
spark.sql("""
    SELECT
        name,
        age,
        CASE
            WHEN age < 30 THEN 'Young'
            WHEN age < 50 THEN 'Middle'
            ELSE 'Senior'
        END as age_group
    FROM employees
""").show()
```

### Subqueries

```python
# Subquery in WHERE
spark.sql("""
    SELECT * FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
""").show()

# Subquery in FROM
spark.sql("""
    SELECT age_group, COUNT(*) as count
    FROM (
        SELECT
            CASE
                WHEN age < 30 THEN 'Young'
                ELSE 'Senior'
            END as age_group
        FROM employees
    )
    GROUP BY age_group
""").show()
```

### Window Functions

```python
# Rank employees by salary
spark.sql("""
    SELECT
        name,
        salary,
        RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
""").show()

# Running total
spark.sql("""
    SELECT
        name,
        salary,
        SUM(salary) OVER (ORDER BY name) as running_total
    FROM employees
""").show()
```

---

## 🎨 Mixing SQL and DataFrame API

```python
# Start with SQL
sql_result = spark.sql("SELECT * FROM employees WHERE age > 30")

# Continue with DataFrame API
final_result = sql_result.select("name", "salary").orderBy("salary")

# Or vice versa
df_result = df.filter(df.age > 30)
df_result.createOrReplaceTempView("filtered")
spark.sql("SELECT AVG(salary) FROM filtered").show()
```

---

## 💡 When to Use SQL vs DataFrame API?

### Use SQL When:

✅ You're comfortable with SQL  
✅ Complex queries are easier to read in SQL  
✅ Working with analysts who know SQL  
✅ Porting existing SQL queries

### Use DataFrame API When:

✅ Building dynamic queries programmatically  
✅ Type safety is important  
✅ IDE autocomplete helps  
✅ Chaining operations

---

## 📝 Quick Reference

### Common SQL Operations

| Operation          | SQL Syntax                                     |
| ------------------ | ---------------------------------------------- |
| **Select all**     | `SELECT * FROM table`                          |
| **Select columns** | `SELECT col1, col2 FROM table`                 |
| **Filter**         | `SELECT * FROM table WHERE condition`          |
| **Sort**           | `SELECT * FROM table ORDER BY col DESC`        |
| **Group**          | `SELECT col, COUNT(*) FROM table GROUP BY col` |
| **Join**           | `SELECT * FROM t1 JOIN t2 ON t1.id = t2.id`    |
| **Limit**          | `SELECT * FROM table LIMIT 10`                 |

---

## 🎯 Practice Exercise

```python
# Create sample data
employees = spark.createDataFrame([
    (1, "Alice", "Engineering", 28, 75000),
    (2, "Bob", "Sales", 35, 65000),
    (3, "Charlie", "Engineering", 42, 95000),
    (4, "Diana", "Sales", 30, 70000),
    (5, "Eve", "Engineering", 28, 72000)
], ["id", "name", "dept", "age", "salary"])

employees.createOrReplaceTempView("employees")

# Tasks (use SQL):
# 1. Find all engineers
# 2. Get average salary by department
# 3. Find top 2 highest earners
# 4. Count employees under 30
# 5. Get employees earning above average

# Solutions:
spark.sql("SELECT * FROM employees WHERE dept = 'Engineering'").show()

spark.sql("""
    SELECT dept, AVG(salary) as avg_salary
    FROM employees
    GROUP BY dept
""").show()

spark.sql("""
    SELECT * FROM employees
    ORDER BY salary DESC
    LIMIT 2
""").show()

spark.sql("SELECT COUNT(*) FROM employees WHERE age < 30").show()

spark.sql("""
    SELECT * FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
""").show()
```

---

_Previous: [← Actions](./03_actions.md) | Next: [Optimization →](./05_optimization.md)_
