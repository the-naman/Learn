"""
01_file_formats.py
==================
Reading and writing different file formats in PySpark.
Parquet is the recommended format for big data workloads.
"""

from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("FileFormats").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Sample data
data = [
    ("Naman",  25, "Engineering", 75000.0),
    ("Priya",  28, "Analytics",   65000.0),
    ("Raj",    30, "Management",  90000.0),
    ("Sneha",  22, "Engineering", 30000.0),
]
df = spark.createDataFrame(data, ["name", "age", "dept", "salary"])

output_base = "output"
os.makedirs(output_base, exist_ok=True)

# ── CSV ───────────────────────────────────────────────────────────────────────
df.write.mode("overwrite").option("header", True).csv(f"{output_base}/employees_csv")
csv_df = spark.read.option("header", True).option("inferSchema", True).csv(f"{output_base}/employees_csv")
print("CSV read back:")
csv_df.show()

# ── JSON ──────────────────────────────────────────────────────────────────────
df.write.mode("overwrite").json(f"{output_base}/employees_json")
json_df = spark.read.json(f"{output_base}/employees_json")
print("JSON read back:")
json_df.show()

# ── Parquet (recommended — columnar, compressed, fast) ────────────────────────
df.write.mode("overwrite").parquet(f"{output_base}/employees_parquet")
parquet_df = spark.read.parquet(f"{output_base}/employees_parquet")
print("Parquet read back:")
parquet_df.show()
parquet_df.printSchema()   # Schema preserved automatically

# ── Partitioned write (splits files by column value) ─────────────────────────
df.write.mode("overwrite").partitionBy("dept").parquet(f"{output_base}/employees_partitioned")
# Creates: employees_partitioned/dept=Engineering/, dept=Analytics/, dept=Management/

# Read only one partition (very fast — Spark skips other folders)
eng_df = spark.read.parquet(f"{output_base}/employees_partitioned/dept=Engineering")
print("Engineering partition only:")
eng_df.show()

spark.stop()
