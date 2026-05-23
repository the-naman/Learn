"""
02_window_functions.py
======================
Window functions — one of the most powerful features in PySpark.
They let you compute values ACROSS rows without collapsing them
(unlike groupBy which reduces to one row per group).
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, rank, dense_rank, row_number, lag, lead,
    avg, sum as spark_sum, round as spark_round, percent_rank
)
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("WindowFunctions").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [
    ("Naman",  "Engineering", 75000),
    ("Sneha",  "Engineering", 30000),
    ("Kavya",  "Engineering", 70000),
    ("Priya",  "Analytics",   65000),
    ("Amit",   "Analytics",   85000),
    ("Neha",   "Analytics",   60000),
    ("Raj",    "Management",  90000),
    ("Vikram", "Management",  95000),
]
df = spark.createDataFrame(data, ["name", "dept", "salary"])

# ── Define windows ────────────────────────────────────────────────────────────
dept_window        = Window.partitionBy("dept").orderBy(col("salary").desc())
dept_window_no_ord = Window.partitionBy("dept")
running_window     = Window.partitionBy("dept").orderBy("salary").rowsBetween(Window.unboundedPreceding, 0)

# ── Ranking functions ─────────────────────────────────────────────────────────
print("Ranking within department:")
df.withColumn("rank",        rank().over(dept_window)) \
  .withColumn("dense_rank",  dense_rank().over(dept_window)) \
  .withColumn("row_number",  row_number().over(dept_window)) \
  .withColumn("pct_rank",    spark_round(percent_rank().over(dept_window), 2)) \
  .show()

# ── Lag and Lead (compare with previous/next row) ─────────────────────────────
print("Lag and Lead (previous and next salary in dept):")
df.withColumn("prev_salary", lag("salary", 1).over(dept_window)) \
  .withColumn("next_salary", lead("salary", 1).over(dept_window)) \
  .show()

# ── Running total ─────────────────────────────────────────────────────────────
print("Running total salary within dept:")
df.withColumn("running_total", spark_sum("salary").over(running_window)).show()

# ── Dept average alongside individual rows ────────────────────────────────────
print("Individual vs dept average:")
df.withColumn("dept_avg", spark_round(avg("salary").over(dept_window_no_ord), 0)) \
  .withColumn("diff_from_avg", col("salary") - col("dept_avg")) \
  .show()

# ── Top 1 per department ──────────────────────────────────────────────────────
print("Highest earner per department:")
df.withColumn("rank", rank().over(dept_window)) \
  .filter(col("rank") == 1) \
  .drop("rank") \
  .show()

spark.stop()
