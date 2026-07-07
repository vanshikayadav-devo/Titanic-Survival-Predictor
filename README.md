# Titanic Survival Predictor

This folder contains the Logistic Regression version of the Titanic Survival Analysis project.

## Overview

The model uses the Titanic dataset to predict whether a passenger survived or not. The script cleans missing values, encodes categorical columns, trains a logistic regression classifier, and prints evaluation metrics.

## Files

- `files/stage2.py` - main training and evaluation script
- `dataset/Titanic_train_dataset.csv` - training dataset used by the model

## Requirements

- Python 3.11+
- pandas
- numpy
- scikit-learn

## How to run

From the project root, run:

```powershell
c:/Users/My Mi Notebook/Titanic-Survival-Analysis/.venv-1/Scripts/python.exe files/stage2.py
```

## What the script does

1. Loads the Titanic dataset.
2. Fills missing values in `Age`, `Fare`, `Cabin`, and `Embarked`.
3. Encodes `Sex`, `Embarked`, and `Cabin`.
4. Splits the data into training and testing sets.
5. Trains a Logistic Regression model.
6. Prints accuracy, precision, recall, F1 score, confusion matrix, and train/test accuracy.

## Notes

- `Cabin` is treated as a categorical feature and encoded after replacing missing values with `Unknown`.
- `Embarked` uses the most frequent value to fill missing entries.
- `LogisticRegression(max_iter=1000)` is used to avoid convergence warnings.

## Model Performance

The latest run of the model produced the following values:

| Metric | Value |
|---|---:|
| Accuracy | 0.8045 |
| Precision | 0.7826 |
| Recall | 0.7297 |
| F1 Score | 0.7552 |

### What these values mean

- **Accuracy** shows the model predicted the correct class about 80% of the time.
- **Precision** shows that when the model predicted survival, it was correct about 78% of the time.
- **Recall** shows that the model found about 73% of the actual survivors.
- **F1 score** balances precision and recall, showing a moderate overall classification quality.

These results suggest the model performs reasonably well, but there is still room to improve recall and overall robustness.
