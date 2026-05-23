"""
01_install_and_verify.py
========================
Run this first to confirm PySpark is installed correctly.

Install steps (run in terminal BEFORE this script):
    1. Install Java 11:
       https://www.oracle.com/java/technologies/downloads/#java11

    2. Set JAVA_HOME environment variable:
       [System.Environment]::SetEnvironmentVariable("JAVA_HOME", "C:\Program Files\Java\jdk-11", "User")

    3. Install PySpark:
       pip install pyspark

    4. Run this script:
       python 01_install_and_verify.py
"""

from pyspark.sql import SparkSession

# Create a SparkSession (entry point to all PySpark functionality)
spark = SparkSession.builder \
    .appName("HelloPySpark") \
    .master("local[*]") \
    .getOrCreate()

# Suppress excessive logs
spark.sparkContext.setLogLevel("ERROR")

print("=" * 50)
print(f"PySpark version : {spark.version}")
print(f"Python version  : {spark.sparkContext.pythonVer}")
print("SparkSession    : OK")
print("=" * 50)

# Create a simple DataFrame
data = [("Naman", 1), ("PySpark", 2), ("Learning", 3)]
df = spark.createDataFrame(data, ["word", "id"])

print("\nSample DataFrame:")
df.show()

print("Setup verified successfully!")
spark.stop()
