"""
01_aggregations.py
==================
Aggregations and GroupBy operations in PySpark.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, count, sum as spark_sum, avg, min, max,
    round as spark_round, countDistinct, collect_list
)

spark = SparkSession.builder.appName("Aggregations").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Naman",  "Engineering", "India",  75000),
    ("Priya",  "Analytics",   "India",  65000),
    ("Raj",    "Management",  "USA",    90000),
    ("Sneha",  "Engineering", "India",  30000),
    ("Amit",   "Analytics",   "USA",    85000),
    ("Kavya",  "Engineering", "USA",    70000),
    ("Vikram", "Management",  "India",  95000),
    ("Neha",   "Analytics",   "India",  60000),
]
df = spark.createDataFrame(data, ["name", "dept", "country", "salary"])

# ── Basic aggregations ────────────────────────────────────────────────────────
print("Overall stats:")
df.agg(
    count("*").alias("total_employees"),
    spark_round(avg("salary"), 2).alias("avg_salary"),
    min("salary").alias("min_salary"),
    max("salary").alias("max_salary"),
    spark_sum("salary").alias("total_payroll"),
    countDistinct("dept").alias("num_depts"),
).show()

# ── GroupBy ───────────────────────────────────────────────────────────────────
print("By department:")
df.groupBy("dept").agg(
    count("*").alias("headcount"),
    spark_round(avg("salary"), 0).alias("avg_salary"),
    max("salary").alias("max_salary"),
    collect_list("name").alias("members"),
).show(truncate=False)

# ── Multi-level GroupBy ───────────────────────────────────────────────────────
print("By dept and country:")
df.groupBy("dept", "country").agg(
    count("*").alias("count"),
    spark_round(avg("salary"), 0).alias("avg_salary"),
).orderBy("dept", "country").show()

# ── Pivot ─────────────────────────────────────────────────────────────────────
print("Pivot — avg salary by dept and country:")
df.groupBy("dept").pivot("country").agg(
    spark_round(avg("salary"), 0)
).show()

spark.stop()
