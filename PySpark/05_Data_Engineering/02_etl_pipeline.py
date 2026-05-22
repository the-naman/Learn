"""
02_etl_pipeline.py
==================
A complete ETL pipeline pattern in PySpark.

Extract  → Read raw data from source
Transform → Clean, validate, enrich the data
Load     → Write processed data to destination
"""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, upper, trim, when, current_timestamp, lit
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

spark = SparkSession.builder.appName("ETLPipeline").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


# ── EXTRACT ───────────────────────────────────────────────────────────────────

def extract(spark: SparkSession) -> DataFrame:
    """Read raw data from source."""
    # Simulating raw messy data
    raw_data = [
        ("  naman  ", "25", "engineering", "75000"),
        ("PRIYA",     "28", "Analytics",   "65000"),
        ("raj",       None, "management",  "90000"),
        ("Sneha",     "22", "Engineering", None),
        ("",          "30", "analytics",   "85000"),   # empty name
        ("Amit",      "-5", "Engineering", "80000"),   # invalid age
    ]
    schema = StructType([
        StructField("name",   StringType(), True),
        StructField("age",    StringType(), True),
        StructField("dept",   StringType(), True),
        StructField("salary", StringType(), True),
    ])
    return spark.createDataFrame(raw_data, schema)


# ── TRANSFORM ─────────────────────────────────────────────────────────────────

def transform(df: DataFrame) -> DataFrame:
    """Clean and enrich the data."""
    return df \
        .withColumn("name",   trim(upper(col("name")))) \
        .withColumn("age",    col("age").cast(IntegerType())) \
        .withColumn("salary", col("salary").cast(DoubleType())) \
        .withColumn("dept",   upper(trim(col("dept")))) \
        .filter(col("name") != "") \
        .filter(col("age").isNotNull() & (col("age") > 0)) \
        .filter(col("salary").isNotNull()) \
        .withColumn("salary_band",
            when(col("salary") >= 80000, "SENIOR")
            .when(col("salary") >= 60000, "MID")
            .otherwise("JUNIOR")
        ) \
        .withColumn("processed_at", current_timestamp())


# ── LOAD ──────────────────────────────────────────────────────────────────────

def load(df: DataFrame, path: str):
    """Write processed data to destination."""
    df.write \
        .mode("overwrite") \
        .partitionBy("dept") \
        .parquet(path)
    print(f"Data written to: {path}")


# ── RUN PIPELINE ──────────────────────────────────────────────────────────────

print("=== ETL Pipeline Start ===")

print("\n[EXTRACT] Raw data:")
raw_df = extract(spark)
raw_df.show()

print("[TRANSFORM] Cleaned data:")
clean_df = transform(raw_df)
clean_df.show()
print(f"Records after cleaning: {clean_df.count()} (from {raw_df.count()} raw)")

print("[LOAD] Writing to parquet...")
load(clean_df, "output/processed_employees")

print("\n=== ETL Pipeline Complete ===")
spark.stop()
