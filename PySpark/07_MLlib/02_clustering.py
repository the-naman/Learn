"""
02_clustering.py
================
KMeans clustering with PySpark MLlib.
Groups employees into clusters based on age and salary.
"""

from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml import Pipeline

spark = SparkSession.builder.appName("Clustering").master("local[*]").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

data = [
    (22, 30000), (24, 35000), (23, 28000), (25, 32000),  # cluster: junior
    (28, 65000), (30, 70000), (29, 68000), (31, 72000),  # cluster: mid
    (35, 90000), (38, 95000), (40, 105000), (36, 88000), # cluster: senior
]
df = spark.createDataFrame(data, ["age", "salary"])

# Assemble features
assembler = VectorAssembler(inputCols=["age", "salary"], outputCol="features_raw")

# Scale features (important for KMeans — salary dominates without scaling)
scaler = StandardScaler(inputCol="features_raw", outputCol="features", withStd=True, withMean=True)

# KMeans with 3 clusters
kmeans = KMeans(featuresCol="features", k=3, seed=42)

pipeline = Pipeline(stages=[assembler, scaler, kmeans])
model = pipeline.fit(df)

# Predict
predictions = model.transform(df)
print("Cluster assignments:")
predictions.select("age", "salary", "prediction").orderBy("prediction", "salary").show()

# Evaluate (Silhouette score: -1 to 1, higher is better)
evaluator = ClusteringEvaluator(featuresCol="features")
silhouette = evaluator.evaluate(predictions)
print(f"Silhouette score: {silhouette:.4f}")

spark.stop()
