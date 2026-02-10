"""
PySpark Basics - Creating a Spark Session and Basic DataFrames

This script demonstrates how to:
1. Initialize a SparkSession
2. Create a DataFrame from a list of data
3. Inspect the DataFrame (show, printSchema)
"""

try:
    from pyspark.sql import SparkSession
    from pyspark.sql.types import StructType, StructField, StringType, IntegerType
except ImportError:
    print("PySpark not installed. Please install it with 'pip install pyspark'")
    exit(1)

def main():
    # 1. Initialize Spark Session
    # .master("local[*]") means use all available cores on your local machine
    spark = SparkSession.builder \
        .appName("SparkBasics") \
        .master("local[*]") \
        .get_all() if hasattr(SparkSession.builder, 'get_all') else SparkSession.builder.getOrCreate()

    print(f"Spark Version: {spark.version}")

    # 2. Create Data
    data = [
        ("Alice", 34, "New York"),
        ("Bob", 45, "London"),
        ("Charlie", 28, "Paris"),
        ("David", 33, "New York"),
        ("Eve", 24, "London")
    ]

    # Define Schema (Explicitly)
    schema = StructType([
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("city", StringType(), True)
    ])

    # 3. Create DataFrame
    df = spark.createDataFrame(data, schema)

    # 4. Basic Inspection
    print("\n--- DataFrame Contents ---")
    df.show()

    print("\n--- Schema ---")
    df.printSchema()

    print("\n--- Summary Statistics ---")
    df.describe().show()

    # Stop the session
    spark.stop()

if __name__ == "__main__":
    main()
