"""
01_spark_sql_basics.py
======================
Run SQL queries directly against PySpark DataFrames
using temporary views.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SparkSQL").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Create sample data
employees = spark.createDataFrame([
    (1, "Naman",  "Engineering", 75000),
    (2, "Priya",  "Analytics",   65000),
    (3, "Raj",    "Management",  90000),
    (4, "Sneha",  "Engineering", 30000),
    (5, "Amit",   "Analytics",   85000),
], ["id", "name", "dept", "salary"])

# ── Register as a temporary view ──────────────────────────────────────────────
employees.createOrReplaceTempView("employees")

# ── Run SQL queries ───────────────────────────────────────────────────────────
print("Basic SELECT:")
spark.sql("SELECT * FROM employees").show()

print("Filter:")
spark.sql("SELECT name, salary FROM employees WHERE salary > 70000").show()

print("GROUP BY:")
spark.sql("""
    SELECT dept,
           COUNT(*) as headcount,
           AVG(salary) as avg_salary,
           MAX(salary) as max_salary
    FROM employees
    GROUP BY dept
    ORDER BY avg_salary DESC
""").show()

print("CASE WHEN:")
spark.sql("""
    SELECT name, salary,
           CASE
               WHEN salary >= 80000 THEN 'Senior'
               WHEN salary >= 60000 THEN 'Mid'
               ELSE 'Junior'
           END as band
    FROM employees
""").show()

print("Subquery:")
spark.sql("""
    SELECT * FROM employees
    WHERE salary > (SELECT AVG(salary) FROM employees)
""").show()

print("CTE (Common Table Expression):")
spark.sql("""
    WITH dept_avg AS (
        SELECT dept, AVG(salary) as avg_sal
        FROM employees
        GROUP BY dept
    )
    SELECT e.name, e.salary, d.avg_sal,
           ROUND(e.salary - d.avg_sal, 2) as diff_from_avg
    FROM employees e
    JOIN dept_avg d ON e.dept = d.dept
""").show()

spark.stop()
