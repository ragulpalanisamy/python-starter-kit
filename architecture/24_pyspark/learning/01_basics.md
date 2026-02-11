# PySpark Basics

> **Getting started with PySpark** - SparkSession, DataFrames, and basic operations

---

## 🚀 Creating a SparkSession

```python
from pyspark.sql import SparkSession

# Create SparkSession (local mode)
spark = SparkSession.builder \
    .appName("MyFirstApp") \
    .master("local[*]") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()

# Verify it works
print(spark.version)  # e.g., 3.5.0
```

**Configuration Options**:

- `.master("local[*]")` - Use all available CPU cores
- `.master("local[4]")` - Use 4 CPU cores
- `.config("key", "value")` - Set Spark configuration

---

## 📊 Creating DataFrames

### From Python List

```python
# Create from list of tuples
data = [
    ("Alice", 28, "NYC"),
    ("Bob", 35, "SF"),
    ("Charlie", 42, "LA")
]

columns = ["name", "age", "city"]

df = spark.createDataFrame(data, columns)
df.show()

# Output:
# +-------+---+----+
# |   name|age|city|
# +-------+---+----+
# |  Alice| 28| NYC|
# |    Bob| 35|  SF|
# |Charlie| 42|  LA|
# +-------+---+----+
```

### From CSV File

```python
# Read CSV with header
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Options:
# - header=True: First row is column names
# - inferSchema=True: Auto-detect data types
# - sep=",": Column separator (default is comma)
```

### From JSON File

```python
df = spark.read.json("data.json")

# For multiline JSON
df = spark.read.option("multiline", "true").json("data.json")
```

### From Dictionary

```python
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [28, 35, 42],
    "city": ["NYC", "SF", "LA"]
}

# Convert to list of Rows
from pyspark.sql import Row

rows = [Row(**{k: v[i] for k, v in data.items()})
        for i in range(len(data["name"]))]

df = spark.createDataFrame(rows)
```

---

## 🔍 Exploring DataFrames

### Show Data

```python
# Show first 20 rows
df.show()

# Show first 5 rows
df.show(5)

# Show without truncating long strings
df.show(truncate=False)

# Show vertically (good for wide DataFrames)
df.show(1, vertical=True)
```

### Schema Information

```python
# Print schema
df.printSchema()

# Output:
# root
#  |-- name: string (nullable = true)
#  |-- age: long (nullable = true)
#  |-- city: string (nullable = true)

# Get column names
df.columns  # ['name', 'age', 'city']

# Get data types
df.dtypes  # [('name', 'string'), ('age', 'bigint'), ...]
```

### Basic Statistics

```python
# Count rows
df.count()  # 3

# Describe numeric columns
df.describe().show()

# Output:
# +-------+------------------+
# |summary|               age|
# +-------+------------------+
# |  count|                 3|
# |   mean|              35.0|
# | stddev|7.0710678118654755|
# |    min|                28|
# |    max|                42|
# +-------+------------------+
```

---

## ✂️ Selecting Columns

```python
# Select single column
df.select("name").show()

# Select multiple columns
df.select("name", "age").show()

# Select with column object
df.select(df.name, df.age).show()

# Select all columns
df.select("*").show()
```

---

## 🔎 Filtering Rows

```python
# Filter with condition
df.filter(df.age > 30).show()

# SQL-style string condition
df.filter("age > 30").show()

# Multiple conditions (AND)
df.filter((df.age > 30) & (df.city == "SF")).show()

# Multiple conditions (OR)
df.filter((df.age > 40) | (df.city == "NYC")).show()

# Not equal
df.filter(df.city != "LA").show()
```

**⚠️ Important**: Use `&` (AND) and `|` (OR), not `and`/`or`. Always use parentheses!

---

## ➕ Adding/Modifying Columns

```python
# Add new column
df = df.withColumn("age_plus_10", df.age + 10)

# Modify existing column
df = df.withColumn("age", df.age + 1)

# Add constant column
from pyspark.sql.functions import lit
df = df.withColumn("country", lit("USA"))

# Rename column
df = df.withColumnRenamed("age", "years")
```

---

## 🗑️ Dropping Columns

```python
# Drop single column
df = df.drop("city")

# Drop multiple columns
df = df.drop("city", "age")
```

---

## 📝 Quick Reference

### Essential Operations

| Operation       | Code                          | Description       |
| --------------- | ----------------------------- | ----------------- |
| **Create**      | `spark.createDataFrame(data)` | Create DataFrame  |
| **Read CSV**    | `spark.read.csv("file.csv")`  | Load CSV file     |
| **Show**        | `df.show()`                   | Display data      |
| **Schema**      | `df.printSchema()`            | Show structure    |
| **Count**       | `df.count()`                  | Count rows        |
| **Select**      | `df.select("col1", "col2")`   | Select columns    |
| **Filter**      | `df.filter(df.age > 30)`      | Filter rows       |
| **Add Column**  | `df.withColumn("new", expr)`  | Add/modify column |
| **Drop Column** | `df.drop("col")`              | Remove column     |

---

## 💡 Best Practices

✅ **Do**:

- Use `inferSchema=True` when reading CSVs
- Chain operations: `df.select("name").filter("age > 30")`
- Use descriptive variable names

❌ **Don't**:

- Use `collect()` on large DataFrames (brings all data to driver)
- Forget parentheses in filter conditions
- Use `and`/`or` instead of `&`/`|`

---

## 🎯 Practice Exercise

```python
# Create a DataFrame
data = [
    ("Alice", 28, "Engineer", 75000),
    ("Bob", 35, "Manager", 85000),
    ("Charlie", 42, "Director", 95000),
    ("Diana", 30, "Engineer", 78000)
]

columns = ["name", "age", "role", "salary"]
df = spark.createDataFrame(data, columns)

# Tasks:
# 1. Show all engineers
# 2. Select name and salary for people over 30
# 3. Add a bonus column (10% of salary)
# 4. Calculate average salary

# Solutions:
df.filter(df.role == "Engineer").show()
df.filter(df.age > 30).select("name", "salary").show()
df.withColumn("bonus", df.salary * 0.1).show()
df.select(avg("salary")).show()
```

---

_Next: [Transformations →](./02_transformations.md)_
