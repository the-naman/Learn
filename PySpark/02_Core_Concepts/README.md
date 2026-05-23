# 02 - Core Concepts

## Topics
- Spark Architecture (Driver, Executor, Cluster Manager)
- RDDs (Resilient Distributed Datasets)
- Transformations vs Actions
- Lazy Evaluation
- DAG (Directed Acyclic Graph)

## Key Mental Model
Spark never does work immediately. It builds a plan (DAG) and
only executes when you call an ACTION (show, count, collect, write).
TRANSFORMATIONS (filter, map, select) just add steps to the plan.
