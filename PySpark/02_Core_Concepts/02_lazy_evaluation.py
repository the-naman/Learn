"""
02_lazy_evaluation.py
=====================
Spark uses LAZY evaluation — transformations build a plan,
actions execute it. This is the core mental model for PySpark.
"""

from pyspark.sql import SparkSession
import time

spark = SparkSession.builder.appName("LazyEval").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
sc = spark.sparkContext

print("Creating RDD and applying transformations...")
print("(Nothing is actually computed yet)\n")

rdd = sc.parallelize(range(1, 1000001))   # 1 million numbers

# These are TRANSFORMATIONS — instant, no computation yet
t1 = time.time()
filtered = rdd.filter(lambda x: x % 2 == 0)
mapped   = filtered.map(lambda x: x ** 2)
t2 = time.time()
print(f"Transformations defined in : {t2-t1:.4f} seconds (just building the plan)")

# This is an ACTION — NOW Spark executes everything
t3 = time.time()
result = mapped.count()
t4 = time.time()
print(f"Action (count) executed in : {t4-t3:.4f} seconds (actual computation)")
print(f"Count of even squares      : {result}")

# Key insight: Spark optimizes the whole plan before executing
# It won't compute filtered then mapped separately —
# it combines them into one pass over the data

spark.stop()
