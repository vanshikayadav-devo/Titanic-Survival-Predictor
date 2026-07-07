# Stage 2: Titanic Survival Model

This script trains a logistic regression model to predict Titanic survival using the training dataset.

## What the script does

1. Loads the Titanic dataset from `dataset/Titanic_train_dataset.csv`.
2. Shows missing values before and after cleaning.
3. Fills missing values:
   - `Age` with the median
   - `Fare` with the mean
   - `Cabin` with `Unknown`
   - `Embarked` with the most frequent value
4. Encodes categorical columns:
   - `Sex`
   - `Embarked`
   - `Cabin`
5. Drops unused columns:
   - `PassengerId`
   - `Name`
   - `Ticket`
   - `Survived` from features
6. Splits the data into training and test sets.
7. Trains a `LogisticRegression` model.
8. Prints evaluation metrics:
   - Accuracy
   - Precision
   - Recall
   - F1 score
   - Confusion matrix
   - Train accuracy
   - Test accuracy

## Why this version works

- `Cabin` is text data, so it is filled with a string value instead of using `.mean()`.
- `Embarked` uses `mode()[0]` because `mode()` returns a Series.
- `LogisticRegression(max_iter=1000)` helps avoid convergence warnings.

## How to run

Use the same Python environment configured for the project and run:

```bash
python files/stage2.py
```

If you are using the workspace virtual environment directly on Windows:

```powershell
c:/Users/My Mi Notebook/Titanic-Survival-Analysis/.venv-1/Scripts/python.exe files/stage2.py
```
