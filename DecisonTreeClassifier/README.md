# Titanic Survival Predictor - Decision Tree Classifier

This project uses a Decision Tree Classifier to predict Titanic survival based on passenger features.

## Overview

The script loads the Titanic training dataset, cleans missing values, encodes categorical columns, trains a decision tree model, and prints evaluation results.

## Files

- `stage1.py` - main decision tree training and evaluation script
- `Logistic-Regression/dataset/Titanic_train_dataset.csv` - dataset used by the model

## Requirements

- Python 3.11+
- pandas
- numpy
- scikit-learn

## How to run

From the project root, run:

```powershell
c:/Users/My Mi Notebook/Titanic-Survival-Analysis/.venv-1/Scripts/python.exe DecisonTreeClassifier/stage1.py
```

## What the script does

1. Loads the Titanic dataset.
2. Fills missing values in `Age`, `Fare`, `Cabin`, and `Embarked`.
3. Encodes `Sex`, `Embarked`, and `Cabin`.
4. Splits the data into training and test sets.
5. Trains a `DecisionTreeClassifier` with `max_depth=3`.
6. Prints accuracy, precision, recall, F1 score, confusion matrix, training accuracy, and testing accuracy.

## Model Results

The latest run produced the following values:

| Metric | Value |
|---|---:|
| Accuracy | 0.7989 |
| Precision | 0.7969 |
| Recall | 0.6892 |
| F1 Score | 0.7391 |
| Training Accuracy | 0.8343 |
| Testing Accuracy | 0.7989 |

Confusion matrix:

```text
[[92 13]
 [23 51]]
```

## Performance Summary

- The model gets about 80% test accuracy, which is a solid result for a simple decision tree.
- Precision is slightly higher than recall, so the model is better at avoiding false positives than finding every survivor.
- The gap between training accuracy and testing accuracy is small, so the model is not strongly overfitting.
- Overall, this is a reasonable baseline model, but recall could be improved with better feature engineering or tuning.
