---
id: "scikit-learn_002"
technology: "scikit-learn"
category: "ML & Data"
title: "Pipelines and Feature Preprocessing in scikit-learn (StandardScaler, Pipeline)"
doc_order: 2
source_url: "https://scikit-learn.org/stable/modules/compose.html#pipeline"
language: "en"
retrieved_at: "2026-11-03 20:47:00"
content_hash: "sklearn_pipeline_preprocessing_002"
---

# Pipelines and Feature Preprocessing in scikit-learn

Source: https://scikit-learn.org/stable/modules/compose.html#pipeline

---

## What is a Pipeline in scikit-learn

A `Pipeline` sequentially applies a list of transformers to preprocess data before passing it to a final estimator (such as a classifier or regressor). Intermediate steps must implement both `fit` and `transform` methods, while the final estimator only requires `fit` (and optionally `predict` or `predict_proba`).

### Why Use Pipelines
- **Prevents Data Leakage**: Transformers are fit exclusively on training folds during cross-validation, avoiding leakage from the test or validation set.
- **Unified Workflow**: You only need to call `fit` and `predict` once on the entire sequence of preprocessing and modeling steps.
- **Convenient Hyperparameter Tuning**: You can grid-search over parameters of all transformers and estimators simultaneously using `GridSearchCV`.

---

## How to Chain Feature Scaling and Logistic Regression in scikit-learn

To chain feature scaling (`StandardScaler`) and a classification model (`LogisticRegression`) together:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# 1. Generate sample classification dataset
X, y = make_classification(n_samples=1000, n_features=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Define the Pipeline with named steps
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

# 3. Fit pipeline on training data (scaler fits & transforms, then classifier fits)
pipeline.fit(X_train, y_train)

# 4. Predict on new test data (scaler transforms automatically, then classifier predicts)
y_pred = pipeline.predict(X_test)

# 5. Evaluate accuracy score
accuracy = pipeline.score(X_test, y_test)
print(f"Test Accuracy: {accuracy:.4f}")
```

Alternatively, you can use the `make_pipeline` shortcut which automatically generates step names based on class names:

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(X_train, y_train)
```

---

## Accessing and Tuning Pipeline Steps

You can access individual steps using the `named_steps` dictionary attribute:

```python
# Access the fitted scaler or classifier
scaler_step = pipeline.named_steps['scaler']
classifier_step = pipeline.named_steps['classifier']

# Inspect coefficients from the classifier
print("Learned Coefficients:", classifier_step.coef_)
```

### Hyperparameter Tuning with Pipeline
To tune parameters of steps inside a pipeline with `GridSearchCV`, prefix the parameter name with the step name followed by double underscores (`<step_name>__<parameter_name>`):

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'scaler__with_mean': [True, False],
    'classifier__C': [0.01, 0.1, 1.0, 10.0],
    'classifier__solver': ['lbfgs', 'liblinear']
}

grid = GridSearchCV(pipeline, param_grid, cv=5)
grid.fit(X_train, y_train)
print("Best parameters:", grid.best_params_)
```

