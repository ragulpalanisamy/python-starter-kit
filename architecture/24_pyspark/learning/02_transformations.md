# PySpark Transformations

> **Data transformation operations** - The core of data processing

---

## 🔄 What are Transformations?

**Transformations** are operations that create a new DataFrame from an existing one. They are **lazy** - they don't execute until an action is called.

```
df.select("name")           ← Transformation (lazy)
  .filter(df.age > 30)      ← Transformation (lazy)
  .show()                   ← Action (triggers execution!)
```

---

## 📋 Common Transformations

### 1. select() - Choose Columns

```python
# Select specific columns
df.select("name", "age")

# Select with expressions
from pyspark.sql.functions import col
df.select(col("name"), col("age") + 1)

# Select and rename
df.select(col("name").alias("full_name"))
```

---

### 2. filter() / where() - Filter Rows

```python
# Simple filter
df.filter(df.age > 30)
df.where(df.age > 30)  # Same as filter

# Multiple conditions
df.filter((df.age > 30) & (df.salary > 50000))

# String contains
df.filter(df.name.contains("Alice"))

# NULL checks
df.filter(df.age.isNotNull())
df.filter(df.age.isNull())
```

---

### 3. withColumn() - Add/Modify Columns

```python
# Add new column
df.withColumn("age_squared", df.age * df.age)

# Modify existing column
df.withColumn("age", df.age + 1)

# Conditional column
from pyspark.sql.functions import when
df.withColumn("age_group",
    when(df.age < 30, "Young")
    .when(df.age < 50, "Middle")
    .otherwise("Senior")
)
```

---

### 4. groupBy() - Group Data

```python
# Group and count
df.groupBy("city").count()

# Group and aggregate
df.groupBy("city").agg({"salary": "avg", "age": "max"})

# Multiple aggregations
from pyspark.sql.functions import avg, max, min, sum
df.groupBy("city").agg(
    avg("salary").alias("avg_salary"),
    max("age").alias("max_age"),
    min("age").alias("min_age")
)
```

---

### 5. orderBy() / sort() - Sort Data

```python
# Sort ascending
df.orderBy("age")
df.sort("age")  # Same as orderBy

# Sort descending
df.orderBy(df.age.desc())

# Multiple columns
df.orderBy("city", df.age.desc())
```

---

### 6. distinct() - Remove Duplicates

```python
# Get unique rows
df.distinct()

# Get unique values from column
df.select("city").distinct()

# Drop duplicates based on columns
df.dropDuplicates(["name", "city"])
```

---

### 7. join() - Combine DataFrames

```python
# Sample DataFrames
employees = spark.createDataFrame([
    (1, "Alice", "Engineering"),
    (2, "Bob", "Sales")
], ["id", "name", "dept"])

salaries = spark.createDataFrame([
    (1, 75000),
    (2, 65000)
], ["id", "salary"])

# Inner join (default)
employees.join(salaries, "id")

# Left join
employees.join(salaries, "id", "left")

# Right join
employees.join(salaries, "id", "right")

# Full outer join
employees.join(salaries, "id", "outer")

# Join on different column names
employees.join(salaries, employees.id == salaries.emp_id)
```

---

### 8. union() - Combine Rows

```python
df1 = spark.createDataFrame([(1, "Alice")], ["id", "name"])
df2 = spark.createDataFrame([(2, "Bob")], ["id", "name"])

# Union (combine rows)
df1.union(df2)

# Output:
# +---+-----+
# | id| name|
# +---+-----+
# |  1|Alice|
# |  2|  Bob|
# +---+-----+
```

---

## 🔧 Built-in Functions

### String Functions

```python
from pyspark.sql.functions import upper, lower, length, concat, substring

# Uppercase
df.withColumn("name_upper", upper(df.name))

# Lowercase
df.withColumn("name_lower", lower(df.name))

# String length
df.withColumn("name_length", length(df.name))

# Concatenate
df.withColumn("full_info", concat(df.name, lit(" - "), df.city))

# Substring
df.withColumn("first_char", substring(df.name, 1, 1))
```

---

### Numeric Functions

```python
from pyspark.sql.functions import round, abs, sqrt, pow

# Round
df.withColumn("salary_rounded", round(df.salary, -3))

# Absolute value
df.withColumn("abs_value", abs(df.value))

# Square root
df.withColumn("sqrt_age", sqrt(df.age))

# Power
df.withColumn("age_squared", pow(df.age, 2))
```

---

### Date Functions

```python
from pyspark.sql.functions import current_date, date_add, datediff, year, month

# Current date
df.withColumn("today", current_date())

# Add days
df.withColumn("next_week", date_add(df.date, 7))

# Date difference
df.withColumn("days_diff", datediff(current_date(), df.date))

# Extract year/month
df.withColumn("year", year(df.date))
df.withColumn("month", month(df.date))
```

---

### Aggregate Functions

```python
from pyspark.sql.functions import avg, max, min, sum, count, countDistinct

# Average
df.select(avg("salary"))

# Max/Min
df.select(max("age"), min("age"))

# Sum
df.select(sum("salary"))

# Count
df.select(count("*"))

# Count distinct
df.select(countDistinct("city"))
```

---

## 🎯 Chaining Transformations

```python
# Chain multiple transformations
result = df \
    .filter(df.age > 25) \
    .select("name", "age", "salary") \
    .withColumn("bonus", df.salary * 0.1) \
    .orderBy(df.salary.desc()) \
    .limit(10)

result.show()
```

**Benefits**:

- Readable code
- Spark optimizes the entire chain
- Easy to modify

---

## 💡 Performance Tips

### 1. Filter Early

```python
# ✅ Good: Filter first
df.filter(df.age > 30).select("name", "salary")

# ❌ Bad: Select then filter
df.select("name", "age", "salary").filter(df.age > 30)
```

### 2. Use Column Pruning

```python
# ✅ Good: Select only needed columns
df.select("name", "age").groupBy("age").count()

# ❌ Bad: Keep all columns
df.groupBy("age").count()
```

### 3. Avoid Collect on Large Data

```python
# ❌ Bad: Brings all data to driver
all_data = df.collect()

# ✅ Good: Process in distributed manner
df.write.parquet("output")
```

---

## 📝 Quick Reference

| Transformation | Purpose           | Example                      |
| -------------- | ----------------- | ---------------------------- |
| `select()`     | Choose columns    | `df.select("name")`          |
| `filter()`     | Filter rows       | `df.filter(df.age > 30)`     |
| `withColumn()` | Add/modify column | `df.withColumn("new", expr)` |
| `groupBy()`    | Group data        | `df.groupBy("city").count()` |
| `orderBy()`    | Sort data         | `df.orderBy("age")`          |
| `join()`       | Join DataFrames   | `df1.join(df2, "id")`        |
| `distinct()`   | Remove duplicates | `df.distinct()`              |
| `union()`      | Combine rows      | `df1.union(df2)`             |

---

## 🎯 Practice Exercise

```python
# Sample data
data = [
    ("Alice", 28, "NYC", 75000),
    ("Bob", 35, "SF", 85000),
    ("Charlie", 42, "NYC", 95000),
    ("Diana", 30, "SF", 78000),
    ("Eve", 28, "LA", 72000)
]

df = spark.createDataFrame(data, ["name", "age", "city", "salary"])

# Tasks:
# 1. Find average salary by city
# 2. Add a "senior" column (True if age > 35)
# 3. Get top 2 highest earners
# 4. Count employees per city

# Solutions:
df.groupBy("city").agg(avg("salary")).show()
df.withColumn("senior", df.age > 35).show()
df.orderBy(df.salary.desc()).limit(2).show()
df.groupBy("city").count().show()
```

---

_Previous: [← Basics](./01_basics.md) | Next: [Actions →](./03_actions.md)_
