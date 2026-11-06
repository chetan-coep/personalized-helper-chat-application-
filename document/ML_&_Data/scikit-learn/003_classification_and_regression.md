---
id: "scikit-learn_003"
technology: "scikit-learn"
category: "ML & Data"
title: "Classification and Regression Estimators in scikit-learn"
doc_order: 3
source_url: "https://scikit-learn.org/stable/supervised_learning.html"
language: "en"
retrieved_at: "2026-11-03 20:47:00"
content_hash: "sklearn_classification_regression_003"
---

# Supervised Classification and Regression in scikit-learn

Source: https://scikit-learn.org/stable/supervised_learning.html

---

## Logistic Regression Classifier

`LogisticRegression` is a linear model for classification that models probabilities using a logistic (sigmoid) function.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Initialize model with L2 regularization
clf = LogisticRegression(C=1.0, solver='lbfgs', max_iter=200, random_state=42)

# Train estimator
clf.fit(X_train, y_train)

# Predict class labels
predictions = clf.predict(X_test)

# Predict probability estimates
probabilities = clf.predict_proba(X_test)

print("Classification Report:")
print(classification_report(y_test, predictions))
```

### Key Parameters of LogisticRegression
- `penalty`: Regularization norm (`'l1'`, `'l2'`, `'elasticnet'`, or `None`). Default is `'l2'`.
- `C`: Inverse of regularization strength (float, default=1.0). Smaller values specify stronger regularization.
- `solver`: Optimization algorithm (`'lbfgs'`, `'liblinear'`, `'saga'`). `'lbfgs'` handles multinomial loss and multiclass classification.
- `max_iter`: Maximum number of iterations taken for the solvers to converge (default=100).
- `random_state`: Seed used by the random number generator.

---

## Random Forest Classifier

`RandomForestClassifier` is an ensemble learning method that fits multiple decision tree classifiers on various sub-samples of the dataset and averages their predictions to improve accuracy and control overfitting.

```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# Feature importances
print("Feature Importances:", rf.feature_importances_)
```

