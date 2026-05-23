"""
02_transformations.py
=====================
Core DataFrame transformations — select, filter, withColumn,
groupBy, orderBy, joins, and handling nulls.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, lower, lit, when, isnull, round as spark_round

spark = SparkSession.builder.appName("Transformations").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Naman",  25, "Engineering", 75000.0),
    ("Priya",  28, "Analytics",   65000.0),
    ("Raj",    30, "Management",  90000.0),
    ("Sneha",  22, "Engineering", 30000.0),
    ("Amit",   35, "Analytics",   85000.0),
    ("Kavya",  None, "Management", None),
]
df = spark.createDataFrame(data, ["name", "age", "dept", "salary"])

# ── select ────────────────────────────────────────────────────────────────────
print("Select name and salary:")
df.select("name", "salary").show()

# ── filter / where ────────────────────────────────────────────────────────────
print("Engineers only:")
df.filter(col("dept") == "Engineering").show()

print("Salary > 70000:")
df.where(col("salary") > 70000).show()

# ── withColumn — add or modify a column ──────────────────────────────────────
print("Add salary in lakhs:")
df.withColumn("salary_lakhs", spark_round(col("salary") / 100000, 2)).show()

print("Uppercase names:")
df.withColumn("name_upper", upper(col("name"))).show()

# ── when / otherwise — conditional column ────────────────────────────────────
print("Salary band:")
df.withColumn("band",
    when(col("salary") >= 80000, "Senior")
    .when(col("salary") >= 60000, "Mid")
    .when(col("salary") < 60000, "Junior")
    .otherwise("Unknown")
).show()

# ── groupBy + aggregation ─────────────────────────────────────────────────────
from pyspark.sql.functions import avg, max, min, count, sum as spark_sum
print("Dept summary:")
df.groupBy("dept").agg(
    count("name").alias("headcount"),
    spark_round(avg("salary"), 2).alias("avg_salary"),
    max("salary").alias("max_salary"),
).show()

# ── orderBy / sort ────────────────────────────────────────────────────────────
print("Sorted by salary desc:")
df.orderBy(col("salary").desc()).show()

# ── Handling nulls ────────────────────────────────────────────────────────────
print("Drop rows with any null:")
df.dropna().show()

print("Fill nulls:")
df.fillna({"age": 0, "salary": 0.0}).show()

spark.stop()
