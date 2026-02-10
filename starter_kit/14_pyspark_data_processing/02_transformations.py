"""
PySpark Transformations - Narrow and Wide Transformations

Demonstrates:
- Narrow transformations: select, filter, withColumn
- Wide transformations: groupBy, orderBy (require data shuffling)
"""

try:
    from pyspark.sql import SparkSession
    import pyspark.sql.functions as F
except ImportError:
    print("PySpark not installed.")
    exit(1)

def main():
    spark = SparkSession.builder.appName("SparkTransformations").master("local[*]").getOrCreate()

    # Sample Data
    data = [
        ("Mobile", "Samsung", 1000, "East"),
        ("Mobile", "iPhone", 1200, "West"),
        ("Laptop", "MacBook", 2500, "East"),
        ("Laptop", "Dell", 1500, "West"),
        ("Tablet", "iPad", 800, "East"),
        ("Mobile", "Samsung", 1000, "West"),
    ]
    
    columns = ["Category", "Product", "Sales", "Region"]
    df = spark.createDataFrame(data, columns)

    print("Original Data:")
    df.show()

    # 1. Narrow Transformations (No Shuffle)
    print("\n--- Narrow Transformations (select, filter, withColumn) ---")
    narrow_df = df.select("Product", "Sales", "Region") \
                .filter(F.col("Sales") > 1000) \
                .withColumn("Sales_Tax", F.col("Sales") * 0.1)
    
    narrow_df.show()

    # 2. Wide Transformations (Requires Shuffle)
    print("\n--- Wide Transformations (groupBy, aggregations) ---")
    # Grouping by Category and summing Sales
    wide_df = df.groupBy("Category") \
                .agg(
                    F.sum("Sales").alias("Total_Sales"),
                    F.avg("Sales").alias("Avg_Sales"),
                    F.count("Product").alias("Product_Count")
                ) \
                .orderBy(F.desc("Total_Sales"))
    
    wide_df.show()

    # Stop the session
    spark.stop()

if __name__ == "__main__":
    main()
