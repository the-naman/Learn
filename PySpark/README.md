# PySpark Learning Journey 🚀
> From complete beginner to Data Engineering + Analysis + ML

---

## What is PySpark?
PySpark is the Python API for **Apache Spark** — a distributed computing engine
that processes massive datasets across multiple machines (or cores) in parallel.
Think of it as pandas — but for data too big to fit in one machine's RAM.

---

## Folder Structure

```
PySpark/
├── 01_Setup/               → Install PySpark, test your environment
├── 02_Core_Concepts/       → RDDs, SparkContext, SparkSession, architecture
├── 03_DataFrames/          → Creating, reading, transforming DataFrames
├── 04_SQL/                 → Spark SQL, views, queries on big data
├── 05_Data_Engineering/    → ETL pipelines, partitioning, file formats
├── 06_Data_Analysis/       → Aggregations, window functions, EDA
├── 07_MLlib/               → Machine learning with Spark MLlib
├── 08_Projects/            → End-to-end real-world projects
└── resources/              → Cheatsheets, links, quick references
```

---

## Learning Roadmap

### Phase 1 — Foundation (Week 1-2)
- [ ] Install and configure PySpark locally
- [ ] Understand Spark architecture (Driver, Executor, Cluster)
- [ ] Learn RDDs (Resilient Distributed Datasets)
- [ ] Master SparkSession and SparkContext
- [ ] Read/write CSV, JSON, Parquet files

### Phase 2 — DataFrames and SQL (Week 3-4)
- [ ] Create and manipulate DataFrames
- [ ] Transformations vs Actions
- [ ] Filtering, selecting, grouping, joining
- [ ] Spark SQL and temporary views
- [ ] Schema definition and enforcement

### Phase 3 — Data Engineering (Week 5-6)
- [ ] Build ETL pipelines
- [ ] Partitioning and bucketing
- [ ] Working with Parquet, Delta, ORC formats
- [ ] Handling nulls, duplicates, data quality
- [ ] Writing production-grade pipelines

### Phase 4 — Data Analysis (Week 7-8)
- [ ] Aggregations and GroupBy
- [ ] Window functions (rank, lag, lead, rolling avg)
- [ ] Exploratory Data Analysis at scale
- [ ] Visualising PySpark results with pandas + matplotlib

### Phase 5 — Machine Learning (Week 9-10)
- [ ] MLlib overview and pipeline API
- [ ] Feature engineering (VectorAssembler, StringIndexer)
- [ ] Classification, Regression, Clustering
- [ ] Model evaluation and tuning
- [ ] Saving and loading ML models

### Phase 6 — Projects (Week 11-12)
- [ ] End-to-end ETL pipeline project
- [ ] Large-scale data analysis project
- [ ] ML pipeline project

---

## Quick Start

```bash
# Install PySpark
pip install pyspark

# Test installation
python -c "import pyspark; print(pyspark.__version__)"

# Start a PySpark shell
pyspark
```

---

## Prerequisites
- Python 3.8+ installed
- Java 8 or 11 installed (required by Spark)
- At least 8GB RAM recommended

---

## Resources
See resources/links.md for curated books, courses, and docs.
