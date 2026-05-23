"""
03_joins.py
===========
All types of DataFrame joins in PySpark.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Joins").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

employees = spark.createDataFrame([
    (1, "Naman",  10),
    (2, "Priya",  20),
    (3, "Raj",    30),
    (4, "Sneha",  99),   # dept 99 doesn't exist
], ["emp_id", "name", "dept_id"])

departments = spark.createDataFrame([
    (10, "Engineering"),
    (20, "Analytics"),
    (30, "Management"),
    (40, "HR"),           # no employee in HR
], ["dept_id", "dept_name"])

print("INNER JOIN (only matching rows):")
employees.join(departments, "dept_id", "inner").show()

print("LEFT JOIN (all employees, matched dept or null):")
employees.join(departments, "dept_id", "left").show()

print("RIGHT JOIN (all departments, matched employee or null):")
employees.join(departments, "dept_id", "right").show()

print("OUTER JOIN (all rows from both):")
employees.join(departments, "dept_id", "outer").show()

print("LEFT ANTI JOIN (employees with NO matching dept):")
employees.join(departments, "dept_id", "left_anti").show()

spark.stop()
