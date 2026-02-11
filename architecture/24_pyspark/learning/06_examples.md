# PySpark Real-World Examples

> **Complete examples** - From basic ETL to ML data preparation

---

## 📊 Example 1: Basic ETL Pipeline

**Scenario**: Load CSV, clean data, transform, and save as Parquet.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, upper, when

# Create SparkSession
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .master("local[*]") \
    .getOrCreate()

# 1. EXTRACT: Load data
df = spark.read.csv("raw_data.csv", header=True, inferSchema=True)

print(f"Original records: {df.count()}")
df.show(5)

# 2. TRANSFORM: Clean and transform
df_clean = df \
    .filter(col("age").isNotNull()) \
    .filter(col("salary") > 0) \
    .withColumn("name", trim(upper(col("name")))) \
    .withColumn("age_group",
        when(col("age") < 30, "Young")
        .when(col("age") < 50, "Middle")
        .otherwise("Senior")
    ) \
    .dropDuplicates(["name", "email"])

print(f"Clean records: {df_clean.count()}")

# 3. LOAD: Save as Parquet
df_clean.write \
    .mode("overwrite") \
    .partitionBy("age_group") \
    .parquet("output/clean_data.parquet")

print("ETL pipeline completed!")
spark.stop()
```

---

## 📈 Example 2: Data Aggregation and Reporting

**Scenario**: Analyze sales data and generate reports.

```python
from pyspark.sql.functions import sum, avg, count, max, min, round

# Load sales data
sales = spark.read.parquet("sales_data.parquet")

# Sample data structure:
# | order_id | customer_id | product | quantity | price | date |

# Report 1: Sales by product
product_sales = sales.groupBy("product").agg(
    sum(col("quantity") * col("price")).alias("total_revenue"),
    sum("quantity").alias("total_units"),
    count("order_id").alias("order_count"),
    round(avg(col("quantity") * col("price")), 2).alias("avg_order_value")
).orderBy(col("total_revenue").desc())

product_sales.show()

# Report 2: Top customers
top_customers = sales.groupBy("customer_id").agg(
    sum(col("quantity") * col("price")).alias("total_spent"),
    count("order_id").alias("order_count")
).orderBy(col("total_spent").desc()).limit(10)

top_customers.show()

# Report 3: Daily sales trend
from pyspark.sql.functions import to_date

daily_sales = sales \
    .withColumn("date", to_date("date")) \
    .groupBy("date").agg(
        sum(col("quantity") * col("price")).alias("daily_revenue"),
        count("order_id").alias("daily_orders")
    ).orderBy("date")

daily_sales.show()

# Save reports
product_sales.write.mode("overwrite").csv("reports/product_sales.csv", header=True)
top_customers.write.mode("overwrite").csv("reports/top_customers.csv", header=True)
daily_sales.write.mode("overwrite").csv("reports/daily_sales.csv", header=True)
```

---

## 🔗 Example 3: Complex Joins

**Scenario**: Join multiple DataFrames to create enriched dataset.

```python
# Load data
customers = spark.read.parquet("customers.parquet")
orders = spark.read.parquet("orders.parquet")
products = spark.read.parquet("products.parquet")

# customers: customer_id, name, city, country
# orders: order_id, customer_id, product_id, quantity, date
# products: product_id, product_name, category, price

# Join all three
enriched = orders \
    .join(customers, "customer_id", "left") \
    .join(products, "product_id", "left") \
    .select(
        "order_id",
        "customer_id",
        col("name").alias("customer_name"),
        "city",
        "country",
        "product_id",
        col("product_name"),
        "category",
        "quantity",
        "price",
        (col("quantity") * col("price")).alias("order_value"),
        "date"
    )

enriched.show()

# Analyze by country and category
country_category = enriched.groupBy("country", "category").agg(
    sum("order_value").alias("total_revenue"),
    count("order_id").alias("order_count")
).orderBy("country", col("total_revenue").desc())

country_category.show()
```

---

## 🧹 Example 4: Data Quality Checks

**Scenario**: Validate data quality and identify issues.

```python
from pyspark.sql.functions import isnan, isnull, when, count

# Load data
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Check 1: Null counts per column
null_counts = df.select([
    count(when(col(c).isNull(), c)).alias(c)
    for c in df.columns
])

print("Null counts:")
null_counts.show()

# Check 2: Duplicate records
total_records = df.count()
unique_records = df.dropDuplicates().count()
duplicates = total_records - unique_records

print(f"Total records: {total_records}")
print(f"Unique records: {unique_records}")
print(f"Duplicates: {duplicates}")

# Check 3: Value ranges
print("\nValue ranges:")
df.select([
    min(c).alias(f"{c}_min"),
    max(c).alias(f"{c}_max")
    for c in df.columns if df.schema[c].dataType.typeName() in ['integer', 'double']
]).show()

# Check 4: Invalid values
invalid_age = df.filter((col("age") < 0) | (col("age") > 120)).count()
invalid_salary = df.filter(col("salary") < 0).count()

print(f"Invalid age records: {invalid_age}")
print(f"Invalid salary records: {invalid_salary}")

# Generate quality report
quality_report = {
    "total_records": total_records,
    "unique_records": unique_records,
    "duplicates": duplicates,
    "invalid_age": invalid_age,
    "invalid_salary": invalid_salary
}

print("\nQuality Report:", quality_report)
```

---

## 🤖 Example 5: ML Data Preparation

**Scenario**: Prepare text data for sentiment analysis with PyTorch.

```python
from pyspark.sql.functions import length, regexp_replace, lower, trim

# Load reviews
reviews = spark.read.json("reviews.json")
# Schema: review_id, text, rating

# Clean text
reviews_clean = reviews \
    .filter(col("text").isNotNull()) \
    .filter(length(col("text")) > 10) \
    .withColumn("text", lower(col("text"))) \
    .withColumn("text", regexp_replace(col("text"), "[^a-zA-Z0-9\\s]", "")) \
    .withColumn("text", trim(col("text"))) \
    .withColumn("label", when(col("rating") >= 4, 1).otherwise(0)) \
    .select("review_id", "text", "label")

# Split train/test (80/20)
train, test = reviews_clean.randomSplit([0.8, 0.2], seed=42)

print(f"Training samples: {train.count()}")
print(f"Test samples: {test.count()}")

# Check label distribution
train.groupBy("label").count().show()

# Save for ML pipeline
train.write.mode("overwrite").parquet("ml_data/train.parquet")
test.write.mode("overwrite").parquet("ml_data/test.parquet")

# Sample for quick testing
sample = train.limit(1000)
sample.write.mode("overwrite").json("ml_data/sample.json")

print("ML data preparation complete!")
```

---

## 📊 Example 6: Window Functions

**Scenario**: Calculate running totals and rankings.

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, sum as _sum

# Load sales data
sales = spark.read.parquet("sales.parquet")

# Define window specifications
window_by_date = Window.orderBy("date")
window_by_product = Window.partitionBy("product").orderBy(col("revenue").desc())

# Add rankings and running totals
result = sales \
    .withColumn("running_total", _sum("revenue").over(window_by_date)) \
    .withColumn("product_rank", rank().over(window_by_product)) \
    .withColumn("row_num", row_number().over(window_by_product))

result.show()

# Get top 3 products by revenue each day
from pyspark.sql.functions import to_date

daily_top_products = sales \
    .withColumn("date", to_date("date")) \
    .withColumn("rank",
        rank().over(Window.partitionBy("date").orderBy(col("revenue").desc()))
    ) \
    .filter(col("rank") <= 3) \
    .select("date", "product", "revenue", "rank")

daily_top_products.orderBy("date", "rank").show()
```

---

## 🎯 Complete Pipeline Example

**Scenario**: End-to-end data pipeline with error handling.

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_spark_session(app_name):
    """Create and return SparkSession"""
    return SparkSession.builder \
        .appName(app_name) \
        .master("local[*]") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()

def load_data(spark, path):
    """Load data with error handling"""
    try:
        df = spark.read.parquet(path)
        logger.info(f"Loaded {df.count()} records from {path}")
        return df
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def transform_data(df):
    """Apply transformations"""
    logger.info("Starting transformations...")

    df_transformed = df \
        .filter(col("age").isNotNull()) \
        .filter(col("salary") > 0) \
        .withColumn("age_group",
            when(col("age") < 30, "Young")
            .when(col("age") < 50, "Middle")
            .otherwise("Senior")
        ) \
        .withColumn("salary_band",
            when(col("salary") < 50000, "Low")
            .when(col("salary") < 100000, "Medium")
            .otherwise("High")
        )

    logger.info(f"Transformed to {df_transformed.count()} records")
    return df_transformed

def save_data(df, path):
    """Save data with partitioning"""
    try:
        df.write \
            .mode("overwrite") \
            .partitionBy("age_group") \
            .parquet(path)
        logger.info(f"Saved data to {path}")
    except Exception as e:
        logger.error(f"Error saving data: {e}")
        raise

def main():
    """Main pipeline"""
    spark = create_spark_session("DataPipeline")

    try:
        # Load
        df = load_data(spark, "input/data.parquet")

        # Transform
        df_transformed = transform_data(df)

        # Save
        save_data(df_transformed, "output/processed_data.parquet")

        logger.info("Pipeline completed successfully!")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise
    finally:
        spark.stop()

if __name__ == "__main__":
    main()
```

---

## 💡 Best Practices Summary

✅ **Always** close SparkSession with `spark.stop()`  
✅ **Use** Parquet for intermediate and final data  
✅ **Cache** DataFrames used multiple times  
✅ **Filter** early to reduce data size  
✅ **Add** logging for production pipelines  
✅ **Handle** errors gracefully  
✅ **Partition** output data for better query performance  
✅ **Monitor** Spark UI during development

---

_Previous: [← Optimization](./05_optimization.md)_
