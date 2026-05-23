"""
01_create_dataframes.py
=======================
Different ways to create PySpark DataFrames.
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("CreateDataFrames").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# ── Method 1: From a Python list ──────────────────────────────────────────────
data = [
    ("Naman",   25, "Engineer", 75000.0),
    ("Priya",   28, "Analyst",  65000.0),
    ("Raj",     30, "Manager",  90000.0),
    ("Sneha",   22, "Intern",   30000.0),
]
columns = ["name", "age", "role", "salary"]

df1 = spark.createDataFrame(data, columns)
print("Method 1 — From list:")
df1.show()
df1.printSchema()

# ── Method 2: With explicit schema ───────────────────────────────────────────
schema = StructType([
    StructField("name",   StringType(),  nullable=False),
    StructField("age",    IntegerType(), nullable=True),
    StructField("role",   StringType(),  nullable=True),
    StructField("salary", DoubleType(),  nullable=True),
])
df2 = spark.createDataFrame(data, schema)
print("Method 2 — With explicit schema:")
df2.printSchema()

# ── Method 3: From CSV file ───────────────────────────────────────────────────
# df3 = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# ── Method 4: From JSON file ──────────────────────────────────────────────────
# df4 = spark.read.json("path/to/file.json")

# ── Method 5: From Parquet file (most efficient format) ──────────────────────
# df5 = spark.read.parquet("path/to/file.parquet")

# ── Useful DataFrame info ─────────────────────────────────────────────────────
print("Shape   : rows =", df1.count(), ", cols =", len(df1.columns))
print("Columns :", df1.columns)
print("Schema  :", df1.dtypes)

spark.stop()
