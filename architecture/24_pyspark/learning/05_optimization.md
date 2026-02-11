# PySpark Optimization

> **Performance tuning** - Make your Spark jobs faster and more efficient

---

## 🎯 Key Optimization Concepts

### 1. Partitioning

**Partitions** are the basic units of parallelism in Spark. More partitions = more parallelism.

```python
# Check number of partitions
df.rdd.getNumPartitions()  # e.g., 8

# Repartition (increases or decreases partitions, causes shuffle)
df = df.repartition(20)

# Coalesce (only decreases partitions, no shuffle - faster!)
df = df.coalesce(5)
```

**When to repartition**:

- After filtering (data is smaller, reduce partitions)
- Before expensive operations (increase parallelism)
- Before writing (control output file count)

```python
# Example: Filter then reduce partitions
df_filtered = df.filter(df.age > 30)  # Data is now smaller
df_filtered = df_filtered.coalesce(4)  # Reduce partitions
```

---

### 2. Caching and Persistence

**Cache** DataFrames that are used multiple times to avoid recomputation.

```python
# Cache in memory
df.cache()

# Persist with storage level
from pyspark import StorageLevel

df.persist(StorageLevel.MEMORY_AND_DISK)  # Spill to disk if needed
df.persist(StorageLevel.MEMORY_ONLY)      # Memory only
df.persist(StorageLevel.DISK_ONLY)        # Disk only

# Unpersist when done
df.unpersist()
```

**When to cache**:

```python
# ✅ Good: DataFrame used multiple times
df.cache()
df.filter(df.age > 30).count()  # Uses cache
df.filter(df.salary > 50000).count()  # Uses cache

# ❌ Bad: DataFrame used only once
df.cache()
df.show()  # Only used once, caching is wasteful
```

---

### 3. Broadcast Joins

When joining a large DataFrame with a small one, **broadcast** the small one to all executors.

```python
from pyspark.sql.functions import broadcast

# Large DataFrame
large_df = spark.read.parquet("large_data.parquet")  # 1GB

# Small DataFrame
small_df = spark.read.csv("small_lookup.csv")  # 10MB

# ❌ Regular join (shuffles both DataFrames)
result = large_df.join(small_df, "id")

# ✅ Broadcast join (no shuffle of large DataFrame!)
result = large_df.join(broadcast(small_df), "id")
```

**Rule of thumb**: Broadcast if DataFrame < 10MB

---

### 4. Avoid Shuffles

**Shuffle** = expensive data movement across network. Minimize it!

**Operations that cause shuffle**:

- `groupBy()`
- `join()` (without broadcast)
- `repartition()`
- `distinct()`
- `orderBy()`

```python
# ❌ Bad: Multiple shuffles
df.groupBy("city").count() \
  .orderBy("count") \
  .repartition(10)

# ✅ Better: Combine operations
df.groupBy("city").count() \
  .orderBy("count")  # One less shuffle
```

---

### 5. Filter Early

Push filters as early as possible in your pipeline.

```python
# ❌ Bad: Filter after expensive operations
df.groupBy("city").agg(avg("salary")) \
  .filter(col("avg(salary)") > 50000)

# ✅ Good: Filter before grouping
df.filter(df.salary > 40000) \  # Reduces data early
  .groupBy("city").agg(avg("salary"))
```

---

### 6. Column Pruning

Select only the columns you need.

```python
# ❌ Bad: Keep all columns
df.groupBy("city").count()

# ✅ Good: Select only needed columns
df.select("city").groupBy("city").count()
```

---

### 7. Use Parquet Format

Parquet is columnar, compressed, and optimized for Spark.

```python
# ❌ Slow: CSV
df = spark.read.csv("data.csv")

# ✅ Fast: Parquet
df = spark.read.parquet("data.parquet")

# Save as Parquet
df.write.mode("overwrite").parquet("output.parquet")
```

**Benefits**:

- Columnar storage (read only needed columns)
- Compression (smaller files)
- Schema embedded (no need to infer)

---

### 8. Predicate Pushdown

Spark automatically pushes filters to data source when possible.

```python
# Spark pushes filter to Parquet reader
# Only reads rows where age > 30 (very efficient!)
df = spark.read.parquet("data.parquet")
df_filtered = df.filter(df.age > 30)
```

---

### 9. Avoid UDFs (Use Built-in Functions)

**UDFs** (User Defined Functions) are slow because they can't be optimized.

```python
# ❌ Slow: UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import IntegerType

def add_ten(x):
    return x + 10

add_ten_udf = udf(add_ten, IntegerType())
df = df.withColumn("age_plus_10", add_ten_udf(df.age))

# ✅ Fast: Built-in function
df = df.withColumn("age_plus_10", df.age + 10)
```

**When you must use UDFs**: Use Pandas UDFs (vectorized, faster)

```python
from pyspark.sql.functions import pandas_udf
import pandas as pd

@pandas_udf(IntegerType())
def add_ten_pandas(x: pd.Series) -> pd.Series:
    return x + 10

df = df.withColumn("age_plus_10", add_ten_pandas(df.age))
```

---

### 10. Partition Skew

**Skew** = uneven data distribution across partitions.

```python
# Check partition sizes
df.rdd.glom().map(len).collect()  # [1000, 1000, 5000, 1000]
# Partition 3 has 5x more data (skewed!)

# Solution: Repartition by a better column
df = df.repartition("city")  # Distribute by city

# Or add salt to skewed key
from pyspark.sql.functions import rand
df = df.withColumn("salt", (rand() * 10).cast("int"))
df = df.repartition("city", "salt")
```

---

## 📊 Monitoring Performance

### Spark UI

```python
# Start your Spark job
# Open browser: http://localhost:4040

# Check:
# - Jobs tab: See stages and tasks
# - Stages tab: See shuffle read/write
# - Storage tab: See cached DataFrames
# - Executors tab: See resource usage
```

### Explain Plan

```python
# See execution plan
df.explain()

# Detailed plan
df.explain(True)

# Look for:
# - Shuffle operations
# - Broadcast joins
# - Pushed filters
```

---

## 💡 Optimization Checklist

### Before Running

✅ Filter early  
✅ Select only needed columns  
✅ Use Parquet format  
✅ Broadcast small DataFrames in joins  
✅ Cache DataFrames used multiple times  
✅ Use built-in functions instead of UDFs  
✅ Check partition count (2-4x number of cores)

### After Running

✅ Check Spark UI for bottlenecks  
✅ Look for shuffle operations  
✅ Check partition skew  
✅ Verify caching is working  
✅ Monitor memory usage

---

## 🎯 Common Performance Issues

| Issue                   | Symptom                   | Solution                   |
| ----------------------- | ------------------------- | -------------------------- |
| **Too many partitions** | Many small tasks          | `coalesce()`               |
| **Too few partitions**  | Long-running tasks        | `repartition()`            |
| **Shuffle overhead**    | Slow joins/groupBy        | Broadcast small DataFrames |
| **Recomputation**       | Same data processed twice | `cache()`                  |
| **Skewed partitions**   | One task takes forever    | Repartition with salt      |
| **Slow UDFs**           | UDF stage is slow         | Use built-in functions     |

---

## 📝 Quick Reference

### Storage Levels

| Level             | Memory | Disk | Serialized | Use Case             |
| ----------------- | ------ | ---- | ---------- | -------------------- |
| `MEMORY_ONLY`     | ✅     | ❌   | ❌         | Fast, fits in memory |
| `MEMORY_AND_DISK` | ✅     | ✅   | ❌         | Safe default         |
| `DISK_ONLY`       | ❌     | ✅   | ❌         | Large data           |
| `MEMORY_ONLY_SER` | ✅     | ❌   | ✅         | Save memory          |

---

## 🎯 Practice Exercise

```python
# Optimize this code
df = spark.read.csv("large_data.csv")
df = df.filter(df.age > 25)
df = df.groupBy("city").agg(avg("salary"))
df = df.orderBy("city")
df.show()
df.filter(col("avg(salary)") > 50000).show()

# Optimized version:
df = spark.read.parquet("large_data.parquet")  # Use Parquet
df = df.select("age", "city", "salary")  # Column pruning
df = df.filter(df.age > 25)  # Filter early
df.cache()  # Cache (used twice)
df_agg = df.groupBy("city").agg(avg("salary").alias("avg_salary"))
df_agg = df_agg.orderBy("city")
df_agg.show()
df_agg.filter(col("avg_salary") > 50000).show()
df.unpersist()  # Clean up
```

---

_Previous: [← Spark SQL](./04_sql.md) | Next: [Examples →](./06_examples.md)_
