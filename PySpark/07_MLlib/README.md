# 07 - Machine Learning with MLlib

## Topics
- MLlib Pipeline API
- Feature engineering (VectorAssembler, StringIndexer, OneHotEncoder)
- Classification (Logistic Regression, Random Forest, Decision Tree)
- Regression (Linear Regression)
- Clustering (KMeans)
- Model evaluation and cross-validation
- Saving and loading models

## Key Mental Model
MLlib uses a Pipeline of Stages (Transformers + Estimators).
You build the pipeline once, fit it on training data,
then use it to transform/predict on new data.
