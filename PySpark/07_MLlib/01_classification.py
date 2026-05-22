"""
01_classification.py
====================
Binary classification with PySpark MLlib.
Predicts whether an employee is "Senior" (salary >= 75000) or not.

Pipeline:
  StringIndexer (dept text -> number)
  -> OneHotEncoder
  -> VectorAssembler (combine all features)
  -> LogisticRegression
  -> Evaluate
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("Classification").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# ── Sample dataset ────────────────────────────────────────────────────────────
data = [
    ("Engineering", 25, 75000), ("Engineering", 28, 85000),
    ("Engineering", 22, 30000), ("Engineering", 35, 95000),
    ("Analytics",   28, 65000), ("Analytics",   32, 80000),
    ("Analytics",   26, 55000), ("Analytics",   38, 90000),
    ("Management",  30, 90000), ("Management",  35, 110000),
    ("Management",  28, 70000), ("Management",  40, 120000),
    ("Engineering", 29, 72000), ("Analytics",   31, 68000),
    ("Management",  33, 95000), ("Engineering", 24, 45000),
]
df = spark.createDataFrame(data, ["dept", "age", "salary"])

# Create label: 1 = Senior (salary >= 75000), 0 = Not Senior
df = df.withColumn("label", when(col("salary") >= 75000, 1.0).otherwise(0.0))
print("Dataset:")
df.show()

# ── Split data ────────────────────────────────────────────────────────────────
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)
print(f"Train: {train_df.count()} rows | Test: {test_df.count()} rows")

# ── Build Pipeline ────────────────────────────────────────────────────────────
# Step 1: Convert dept string to numeric index
dept_indexer = StringIndexer(inputCol="dept", outputCol="dept_idx", handleInvalid="keep")

# Step 2: One-hot encode the index
dept_encoder = OneHotEncoder(inputCol="dept_idx", outputCol="dept_vec")

# Step 3: Combine all features into one vector
assembler = VectorAssembler(
    inputCols=["dept_vec", "age", "salary"],
    outputCol="features"
)

# Step 4: Logistic Regression model
lr = LogisticRegression(featuresCol="features", labelCol="label", maxIter=10)

# Build pipeline
pipeline = Pipeline(stages=[dept_indexer, dept_encoder, assembler, lr])

# ── Train ─────────────────────────────────────────────────────────────────────
model = pipeline.fit(train_df)
print("Model trained!")

# ── Predict ───────────────────────────────────────────────────────────────────
predictions = model.transform(test_df)
print("\nPredictions:")
predictions.select("dept", "age", "salary", "label", "prediction", "probability").show(truncate=False)

# ── Evaluate ──────────────────────────────────────────────────────────────────
evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction")
accuracy = evaluator.evaluate(predictions, {evaluator.metricName: "accuracy"})
print(f"Accuracy: {accuracy:.2%}")

# ── Save model ────────────────────────────────────────────────────────────────
model.write().overwrite().save("output/lr_model")
print("Model saved to output/lr_model")

spark.stop()
