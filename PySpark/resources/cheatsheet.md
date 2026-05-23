# PySpark Cheatsheet

## SparkSession
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("App").master("local[*]").getOrCreate()
spark.stop()
```

## Create DataFrame
```python
df = spark.createDataFrame(data, ["col1", "col2"])
df = spark.read.csv("file.csv", header=True, inferSchema=True)
df = spark.read.json("file.json")
df = spark.read.parquet("file.parquet")
```

## Inspect
```python
df.show()                  # print rows
df.show(n=10, truncate=False)
df.printSchema()           # column types
df.dtypes                  # list of (name, type)
df.columns                 # list of column names
df.count()                 # number of rows
df.describe().show()       # stats summary
```

## Select and Filter
```python
df.select("col1", "col2")
df.select(col("col1"), col("col2").alias("new_name"))
df.filter(col("age") > 25)
df.where(col("dept") == "Engineering")
df.filter((col("age") > 25) & (col("salary") > 50000))
```

## Transform Columns
```python
df.withColumn("new_col", col("salary") * 1.1)
df.withColumn("upper_name", upper(col("name")))
df.withColumnRenamed("old", "new")
df.drop("col_to_remove")
```

## Conditional
```python
from pyspark.sql.functions import when
df.withColumn("band",
    when(col("salary") >= 80000, "Senior")
    .when(col("salary") >= 60000, "Mid")
    .otherwise("Junior")
)
```

## GroupBy and Aggregation
```python
from pyspark.sql.functions import count, avg, sum, max, min
df.groupBy("dept").agg(
    count("*").alias("headcount"),
    avg("salary").alias("avg_sal"),
    max("salary").alias("max_sal"),
)
```

## Joins
```python
df1.join(df2, "common_col", "inner")
df1.join(df2, "common_col", "left")
df1.join(df2, "common_col", "right")
df1.join(df2, "common_col", "outer")
df1.join(df2, "common_col", "left_anti")
```

## Window Functions
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import rank, lag, avg

w = Window.partitionBy("dept").orderBy(col("salary").desc())
df.withColumn("rank", rank().over(w))
df.withColumn("prev_sal", lag("salary", 1).over(w))
df.withColumn("dept_avg", avg("salary").over(Window.partitionBy("dept")))
```

## Null Handling
```python
df.dropna()                          # drop rows with any null
df.dropna(subset=["col1", "col2"])   # drop rows with null in specific cols
df.fillna(0)                         # fill all nulls with 0
df.fillna({"age": 0, "name": "unknown"})
df.filter(col("age").isNotNull())
df.filter(col("age").isNull())
```

## Write
```python
df.write.mode("overwrite").csv("output/")
df.write.mode("overwrite").json("output/")
df.write.mode("overwrite").parquet("output/")
df.write.mode("overwrite").partitionBy("dept").parquet("output/")
# modes: overwrite, append, ignore, error
```

## SQL
```python
df.createOrReplaceTempView("my_table")
spark.sql("SELECT * FROM my_table WHERE salary > 70000").show()
```

## Useful Functions
```python
from pyspark.sql.functions import (
    col, lit, upper, lower, trim, length,
    round, abs, sqrt, log,
    to_date, date_format, month, year, datediff,
    concat, concat_ws, split, regexp_replace,
    when, coalesce, isnull, isnan,
    count, countDistinct, sum, avg, min, max,
    rank, dense_rank, row_number, lag, lead,
    collect_list, collect_set, explode,
    current_timestamp, current_date,
)
```
