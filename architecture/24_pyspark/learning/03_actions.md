# PySpark Actions

> **Triggering execution** - Actions that compute results

---

## ⚡ What are Actions?

**Actions** are operations that trigger the execution of transformations and return results to the driver or write data to storage.

```
Transformations (Lazy)          Actions (Eager)
      ↓                              ↓
df.select("name")              df.show()
df.filter(df.age > 30)         df.count()
df.groupBy("city")             df.collect()
                               df.write.csv()
      ↓                              ↓
Nothing happens yet!           Execution starts!
```

---

## 📊 Common Actions

### 1. show() - Display Data

```python
# Show first 20 rows (default)
df.show()

# Show first 5 rows
df.show(5)

# Show without truncating
df.show(truncate=False)

# Show vertically (good for wide tables)
df.show(1, vertical=True)

# Output:
# +-------+---+----+
# |   name|age|city|
# +-------+---+----+
# |  Alice| 28| NYC|
# |    Bob| 35|  SF|
# +-------+---+----+
```

---

### 2. count() - Count Rows

```python
# Count total rows
total = df.count()
print(f"Total rows: {total}")  # Total rows: 100

# Count after filtering
filtered_count = df.filter(df.age > 30).count()
```

---

### 3. collect() - Bring Data to Driver

```python
# Collect all rows as list of Row objects
rows = df.collect()

# Access data
for row in rows:
    print(row.name, row.age)

# Convert to dictionary
row_dict = rows[0].asDict()
print(row_dict)  # {'name': 'Alice', 'age': 28, 'city': 'NYC'}
```

**⚠️ Warning**: `collect()` brings ALL data to driver memory. Use only with small DataFrames!

---

### 4. first() / head() - Get First Row(s)

```python
# Get first row
first_row = df.first()
print(first_row.name)  # Alice

# Get first N rows
first_5 = df.head(5)  # Returns list of Row objects

# Get first row as list
first_as_list = df.take(1)
```

---

### 5. take() - Get First N Rows

```python
# Get first 3 rows
rows = df.take(3)

# Similar to head() but more explicit
for row in rows:
    print(row)
```

---

### 6. write - Save Data

#### Save as CSV

```python
# Save as CSV
df.write.csv("output.csv", header=True)

# With options
df.write \
    .mode("overwrite") \
    .option("header", "true") \
    .option("sep", ",") \
    .csv("output.csv")
```

#### Save as Parquet

```python
# Save as Parquet (recommended for big data)
df.write.parquet("output.parquet")

# With compression
df.write \
    .mode("overwrite") \
    .option("compression", "snappy") \
    .parquet("output.parquet")
```

#### Save as JSON

```python
# Save as JSON
df.write.json("output.json")

# Pretty print
df.write \
    .mode("overwrite") \
    .option("pretty", "true") \
    .json("output.json")
```

#### Write Modes

```python
# Overwrite existing data
df.write.mode("overwrite").parquet("output")

# Append to existing data
df.write.mode("append").parquet("output")

# Error if exists (default)
df.write.mode("error").parquet("output")

# Ignore if exists
df.write.mode("ignore").parquet("output")
```

---

### 7. foreach() / foreachPartition() - Apply Function

```python
# Apply function to each row
def print_row(row):
    print(f"{row.name}: {row.age}")

df.foreach(print_row)

# Apply function to each partition (more efficient)
def process_partition(partition):
    for row in partition:
        # Process row
        pass

df.foreachPartition(process_partition)
```

---

### 8. Aggregation Actions

```python
from pyspark.sql.functions import avg, max, min, sum

# Get single value
avg_age = df.select(avg("age")).collect()[0][0]
print(f"Average age: {avg_age}")

# Multiple aggregations
stats = df.agg(
    avg("age").alias("avg_age"),
    max("salary").alias("max_salary"),
    min("salary").alias("min_salary")
).collect()[0]

print(stats.avg_age, stats.max_salary, stats.min_salary)
```

---

### 9. describe() - Summary Statistics

```python
# Get summary statistics
df.describe().show()

# Output:
# +-------+------------------+------------------+
# |summary|               age|            salary|
# +-------+------------------+------------------+
# |  count|               100|               100|
# |   mean|              35.5|           75000.0|
# | stddev|7.0710678118654755|          10000.0|
# |    min|                28|             65000|
# |    max|                42|             95000|
# +-------+------------------+------------------+

# Specific columns
df.describe("age", "salary").show()
```

---

### 10. toPandas() - Convert to Pandas

```python
# Convert to Pandas DataFrame
pandas_df = df.toPandas()

# Now use pandas operations
print(pandas_df.head())
print(pandas_df.describe())
```

**⚠️ Warning**: Like `collect()`, this brings all data to driver. Use only with small DataFrames!

---

## 🎯 When to Use Each Action

| Action       | Use Case      | Data Size  |
| ------------ | ------------- | ---------- |
| `show()`     | Preview data  | Any        |
| `count()`    | Get row count | Any        |
| `collect()`  | Get all data  | Small only |
| `first()`    | Get one row   | Any        |
| `take(n)`    | Get few rows  | Any        |
| `write()`    | Save results  | Any        |
| `toPandas()` | Use pandas    | Small only |

---

## 💡 Performance Tips

### 1. Avoid Unnecessary Actions

```python
# ❌ Bad: Multiple actions
df.count()  # Action 1
df.show()   # Action 2 (re-computes everything!)

# ✅ Good: Cache if using multiple actions
df.cache()
df.count()  # Computes and caches
df.show()   # Uses cache
```

### 2. Use Sampling for Preview

```python
# ❌ Bad: Collect all data to preview
all_data = df.collect()
print(all_data[:10])

# ✅ Good: Use show() or take()
df.show(10)
df.take(10)
```

### 3. Limit Before Collect

```python
# ❌ Bad: Collect everything
all_rows = df.collect()

# ✅ Good: Limit first
sample_rows = df.limit(100).collect()
```

---

## 🔄 Lazy vs Eager Evaluation

```python
# All lazy (nothing executes)
df1 = df.select("name", "age")
df2 = df1.filter(df1.age > 30)
df3 = df2.orderBy("age")

# First action triggers execution of entire chain
df3.show()  # ← Everything executes here!

# Subsequent actions re-execute (unless cached)
df3.count()  # ← Re-executes entire chain!

# Solution: Cache
df3.cache()
df3.show()   # Executes and caches
df3.count()  # Uses cache (fast!)
```

---

## 📝 Quick Reference

| Action       | Returns   | Brings to Driver? |
| ------------ | --------- | ----------------- |
| `show()`     | None      | Few rows          |
| `count()`    | Integer   | Yes (count only)  |
| `collect()`  | List[Row] | Yes (all data) ⚠️ |
| `first()`    | Row       | Yes (1 row)       |
| `take(n)`    | List[Row] | Yes (n rows)      |
| `write()`    | None      | No                |
| `foreach()`  | None      | No                |
| `toPandas()` | DataFrame | Yes (all data) ⚠️ |

---

## 🎯 Practice Exercise

```python
# Sample data
data = [
    ("Alice", 28, 75000),
    ("Bob", 35, 85000),
    ("Charlie", 42, 95000),
    ("Diana", 30, 78000)
]

df = spark.createDataFrame(data, ["name", "age", "salary"])

# Tasks:
# 1. Show first 2 rows
# 2. Count total employees
# 3. Get average salary (single value)
# 4. Save as parquet
# 5. Get highest earner's name

# Solutions:
df.show(2)
print(df.count())
avg_sal = df.select(avg("salary")).collect()[0][0]
df.write.mode("overwrite").parquet("employees.parquet")
top_earner = df.orderBy(df.salary.desc()).first().name
```

---

_Previous: [← Transformations](./02_transformations.md) | Next: [Spark SQL →](./04_sql.md)_
