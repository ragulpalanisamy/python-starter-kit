# 🔥 PySpark Data Processing

> **Apache Spark with Python** - Distributed data processing made simple

---

## 📖 What is PySpark?

**PySpark** is the Python API for Apache Spark, a powerful distributed computing framework for processing large-scale data.

```
┌─────────────────────────────────────────────────────────────┐
│                    Why PySpark?                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ⚡ Speed: 100x faster than traditional MapReduce           │
│  📊 Scale: Process terabytes of data                        │
│  🐍 Python: Easy to learn, powerful to use                  │
│  🔄 Unified: Batch + Streaming + ML in one framework        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Spark Architecture

### Cluster Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     Driver Program                           │
│                   (Your Python Code)                         │
│                                                              │
│  • Creates SparkSession                                     │
│  • Defines transformations                                  │
│  • Triggers actions                                         │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                  Cluster Manager                             │
│              (YARN / Mesos / Standalone)                     │
│                                                              │
│  • Allocates resources                                      │
│  • Manages executors                                        │
└───────────────────────┬──────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┬──────────────┐
        ▼                               ▼              ▼
┌──────────────┐              ┌──────────────┐  ┌──────────────┐
│  Executor 1  │              │  Executor 2  │  │  Executor N  │
│              │              │              │  │              │
│  • Cache     │              │  • Cache     │  │  • Cache     │
│  • Tasks     │              │  • Tasks     │  │  • Tasks     │
└──────────────┘              └──────────────┘  └──────────────┘
```

### Local Mode (For Learning)

```
┌──────────────────────────────────────────────────────────────┐
│              Single Machine (Your Laptop)                    │
│                                                              │
│  Driver + Executor run on same machine                      │
│  Perfect for learning and development                       │
│  No cluster setup required!                                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎯 Core Concepts

### 1. SparkSession

The entry point to Spark functionality.

```python
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("MyApp") \
    .master("local[*]") \
    .getOrCreate()
```

**Key Points**:

- `local[*]` = Use all CPU cores on local machine
- `appName` = Name shown in Spark UI
- `getOrCreate()` = Reuse existing session if available

---

### 2. DataFrames

Distributed collection of data organized into named columns.

```
┌─────────────────────────────────────────────────────────────┐
│                    DataFrame                                 │
├─────────────┬─────────────┬─────────────┬──────────────────┤
│    name     │     age     │    city     │     salary       │
├─────────────┼─────────────┼─────────────┼──────────────────┤
│   Alice     │     28      │   NYC       │    75000         │
│   Bob       │     35      │   SF        │    85000         │
│   Charlie   │     42      │   LA        │    95000         │
└─────────────┴─────────────┴─────────────┴──────────────────┘

Distributed across multiple machines (partitions)
```

---

### 3. Transformations vs Actions

```
┌──────────────────────────────────────────────────────────────┐
│                   TRANSFORMATIONS                            │
│                   (Lazy - Not Executed)                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  • select()    - Select columns                             │
│  • filter()    - Filter rows                                │
│  • groupBy()   - Group data                                 │
│  • join()      - Join DataFrames                            │
│  • orderBy()   - Sort data                                  │
│                                                              │
│  ⚠️  Nothing happens until an ACTION is called!             │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                      ACTIONS                                 │
│                  (Eager - Executed)                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  • show()      - Display data                               │
│  • count()     - Count rows                                 │
│  • collect()   - Bring data to driver                       │
│  • write()     - Save to disk                               │
│                                                              │
│  ✅ Triggers execution of all transformations               │
└──────────────────────────────────────────────────────────────┘
```

---

## 📊 Data Processing Flow

```
1. Load Data
   ↓
   df = spark.read.csv("data.csv", header=True)

2. Transform (Lazy)
   ↓
   df_filtered = df.filter(df.age > 30)
   df_selected = df_filtered.select("name", "salary")

3. Action (Execution)
   ↓
   df_selected.show()  ← All transformations execute here!

4. Output
   ↓
   Results displayed or saved
```

---

## 🔧 Common Operations

### Reading Data

```python
# CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# JSON
df = spark.read.json("data.json")

# Parquet (Optimized format)
df = spark.read.parquet("data.parquet")
```

### Transformations

```python
# Select columns
df.select("name", "age")

# Filter rows
df.filter(df.age > 30)
df.filter("age > 30")  # SQL-style

# Add new column
df.withColumn("age_plus_10", df.age + 10)

# Rename column
df.withColumnRenamed("old_name", "new_name")

# Group and aggregate
df.groupBy("city").agg({"salary": "avg"})
```

### Actions

```python
# Show first 20 rows
df.show()

# Count rows
df.count()

# Collect to driver (⚠️ Use carefully with large data!)
rows = df.collect()

# Save data
df.write.csv("output.csv")
df.write.parquet("output.parquet")
```

---

## 🚀 Performance Tips

### 1. Partitioning

```python
# Repartition for better parallelism
df = df.repartition(10)

# Coalesce to reduce partitions (no shuffle)
df = df.coalesce(2)
```

### 2. Caching

```python
# Cache frequently used DataFrames
df.cache()
df.count()  # First action: computes and caches
df.show()   # Second action: uses cache (faster!)
```

### 3. Broadcast Joins

```python
from pyspark.sql.functions import broadcast

# Broadcast small DataFrame for faster joins
df_large.join(broadcast(df_small), "id")
```

---

## 📚 Learning Path

| Step | Topic                   | Documentation                                  |
| :--- | :---------------------- | :--------------------------------------------- |
| 1    | **Basics**              | [View Guide](./learning/01_basics.md)          |
| 2    | **Transformations**     | [View Guide](./learning/02_transformations.md) |
| 3    | **Actions**             | [View Guide](./learning/03_actions.md)         |
| 4    | **Spark SQL**           | [View Guide](./learning/04_sql.md)             |
| 5    | **Optimization**        | [View Guide](./learning/05_optimization.md)    |
| 6    | **Real-World Examples** | [View Guide](./learning/06_examples.md)        |

---

## 🎓 Quick Reference

### When to Use PySpark?

✅ **Use PySpark when**:

- Processing large datasets (GBs to TBs)
- Need distributed computing
- Working with big data pipelines
- Preparing data for ML at scale

❌ **Don't use PySpark when**:

- Data fits in memory (< 1GB)
- Simple pandas operations suffice
- Overhead not worth it for small tasks

---

## 🔗 Resources

- [Official PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html)

---

_Updated: Feb 2026_
