"""
Project 1: Sales ETL Pipeline
==============================
Complete end-to-end ETL pipeline for sales data.
"""

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import (
    col, trim, upper, when, round as spark_round,
    month, year, to_date, current_timestamp,
    sum as spark_sum, avg, count
)

spark = SparkSession.builder \
    .appName("SalesETLPipeline") \
    .master("local[*]") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")


def extract(spark: SparkSession) -> DataFrame:
    raw = [
        ("2024-01-15", "P001", "Laptop",      "North", 2,  55000.0),
        ("2024-01-20", "P002", "Phone",        "South", 5,  15000.0),
        ("2024-02-10", "P001", "Laptop",       "East",  1,  55000.0),
        ("2024-02-14", "P003", "Tablet",       "North", 3,  25000.0),
        ("2024-02-28", "P002", "  phone  ",    "West",  2,  15000.0),
        ("2024-03-05", "P004", "Headphones",   "South", 10, 3000.0),
        ("2024-03-12", None,   "Laptop",       "North", 1,  55000.0),
        ("2024-03-18", "P003", "Tablet",       "East",  -1, 25000.0),
        ("bad-date",   "P001", "Laptop",       "North", 1,  55000.0),
    ]
    return spark.createDataFrame(
        raw, ["sale_date","product_id","product_name","region","quantity","unit_price"]
    )


def transform(df: DataFrame) -> DataFrame:
    return df \
        .withColumn("sale_date",    to_date(col("sale_date"), "yyyy-MM-dd")) \
        .withColumn("product_name", upper(trim(col("product_name")))) \
        .filter(col("sale_date").isNotNull()) \
        .filter(col("product_id").isNotNull()) \
        .filter(col("quantity") > 0) \
        .withColumn("revenue",     spark_round(col("quantity") * col("unit_price"), 2)) \
        .withColumn("sale_month",  month(col("sale_date"))) \
        .withColumn("sale_year",   year(col("sale_date"))) \
        .withColumn("revenue_band",
            when(col("revenue") >= 100000, "HIGH")
            .when(col("revenue") >= 30000,  "MEDIUM")
            .otherwise("LOW")
        ) \
        .withColumn("processed_at", current_timestamp())


def aggregate(df: DataFrame) -> DataFrame:
    return df.groupBy("product_name", "region", "sale_year", "sale_month").agg(
        count("*").alias("num_transactions"),
        spark_sum("quantity").alias("total_units"),
        spark_round(spark_sum("revenue"), 2).alias("total_revenue"),
        spark_round(avg("revenue"), 2).alias("avg_order_value"),
    ).orderBy("sale_year", "sale_month", col("total_revenue").desc())


def load(df: DataFrame, path: str):
    df.write.mode("overwrite").partitionBy("sale_year", "sale_month").parquet(path)
    print(f"Written to: {path}")


print("=== Sales ETL Pipeline ===")
raw_df   = extract(spark)
clean_df = transform(raw_df)
print(f"Raw: {raw_df.count()} records | Clean: {clean_df.count()} records")
clean_df.show()
agg_df   = aggregate(clean_df)
agg_df.show()
load(agg_df, "output/sales_summary")
print("=== Pipeline Complete ===")
spark.stop()
