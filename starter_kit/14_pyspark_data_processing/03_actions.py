"""
PySpark Actions - Getting results out of Spark

Demonstrates:
- collect(): Returns all rows to the driver
- count(): Returns the number of rows
- take(n): Returns the first n rows
- first(): Returns the first row
"""

try:
    from pyspark.sql import SparkSession
except ImportError:
    print("PySpark not installed.")
    exit(1)

def main():
    spark = SparkSession.builder.appName("SparkActions").master("local[*]").getOrCreate()

    data = range(1, 101) # 1 to 100
    df = spark.createDataFrame([(i,) for i in data], ["number"])

    # 1. Action: count()
    total_count = df.count()
    print(f"\nAction: total count = {total_count}")

    # 2. Action: first()
    first_row = df.first()
    print(f"Action: first row = {first_row}")

    # 3. Action: take(n)
    top_5 = df.take(5)
    print(f"Action: take(5) = {top_5}")

    # 4. Action: collect()
    # WARNING: Use collect() only on small datasets! It pulls data to driver memory.
    even_numbers = df.filter("number % 2 == 0").limit(10).collect()
    print("\nAction: collect() first 10 even numbers:")
    for row in even_numbers:
        print(row[0], end=" ")
    print()

    # Stop the session
    spark.stop()

if __name__ == "__main__":
    main()
