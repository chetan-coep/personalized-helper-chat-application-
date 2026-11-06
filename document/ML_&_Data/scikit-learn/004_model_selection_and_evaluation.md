---
id: "scikit-learn_004"
technology: "scikit-learn"
category: "ML & Data"
title: "Model Selection and Evaluation in scikit-learn (train_test_split, cross-validation, metrics)"
doc_order: 4
source_url: "https://scikit-learn.org/stable/model_selection.html"
language: "en"
retrieved_at: "2026-11-03 20:47:00"
content_hash: "sklearn_model_selection_004"
---

# Model Selection and Evaluation in scikit-learn

Source: https://scikit-learn.org/stable/model_selection.html

---

## Train/Test Data Splitting

`train_test_split` splits arrays or matrices into random train and test subsets with optional stratified sampling:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y  # Preserves class proportions in train and test splits
)
```

---

## K-Fold Cross-Validation

Cross-validation provides an estimate of model performance on unseen data by training and testing on multiple partitions:

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=500)
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

print(f"5-Fold CV Accuracy: {scores.mean():.4f} +/- {scores.std():.4f}")
```

---

## Evaluation Metrics

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
cm = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {acc:.4f}")
print(f"F1 Score: {f1:.4f}")
print("Confusion Matrix:\n", cm)
```

