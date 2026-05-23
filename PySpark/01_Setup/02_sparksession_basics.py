"""
02_sparksession_basics.py
=========================
Learn SparkSession — the entry point to PySpark.
Every PySpark program starts with creating a SparkSession.
"""

from pyspark.sql import SparkSession

# ── Creating a SparkSession ───────────────────────────────────────────────────
spark = SparkSession.builder \
    .appName("SparkSessionBasics") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# ── SparkSession properties ───────────────────────────────────────────────────
print("App Name   :", spark.sparkContext.appName)
print("Master     :", spark.sparkContext.master)
print("Version    :", spark.version)
print("Partitions :", spark.conf.get("spark.sql.shuffle.partitions"))

# ── Getting an existing session (singleton pattern) ───────────────────────────
spark2 = SparkSession.builder.getOrCreate()
print("\nSame session?", spark is spark2)   # True — always reuses existing

# ── SparkContext (low-level API, rarely used directly) ────────────────────────
sc = spark.sparkContext
print("\nSparkContext:", sc)

# ── Always stop the session when done ─────────────────────────────────────────
spark.stop()
print("\nSession stopped.")
