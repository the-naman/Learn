"""
01_rdd_basics.py
================
RDD = Resilient Distributed Dataset
The original low-level PySpark API.
Modern code uses DataFrames, but understanding RDDs helps you
understand what Spark is doing under the hood.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDDBasics").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
sc = spark.sparkContext

# ── Creating RDDs ─────────────────────────────────────────────────────────────

# From a Python list
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
print("RDD from list:", rdd1.collect())

# From a text file
# rdd2 = sc.textFile("path/to/file.txt")

# ── Transformations (LAZY — not executed yet) ─────────────────────────────────

# map: apply a function to each element
doubled = rdd1.map(lambda x: x * 2)

# filter: keep elements that match a condition
evens = rdd1.filter(lambda x: x % 2 == 0)

# flatMap: like map but flattens the result
words = sc.parallelize(["hello world", "pyspark is great"])
word_list = words.flatMap(lambda line: line.split(" "))

# ── Actions (TRIGGER execution) ───────────────────────────────────────────────

print("Doubled     :", doubled.collect())       # collect brings data to driver
print("Evens       :", evens.collect())
print("Words       :", word_list.collect())
print("Count       :", rdd1.count())
print("Sum         :", rdd1.reduce(lambda a, b: a + b))
print("First       :", rdd1.first())
print("Take 3      :", rdd1.take(3))

# ── Key-Value RDDs ────────────────────────────────────────────────────────────
pairs = sc.parallelize([("a", 1), ("b", 2), ("a", 3), ("b", 4)])

# reduceByKey: aggregate values for each key
totals = pairs.reduceByKey(lambda a, b: a + b)
print("\nReduceByKey:", totals.collect())

# groupByKey: group values by key (less efficient than reduceByKey)
grouped = pairs.groupByKey().mapValues(list)
print("GroupByKey :", grouped.collect())

# sortByKey
sorted_rdd = pairs.sortByKey()
print("SortByKey  :", sorted_rdd.collect())

spark.stop()
