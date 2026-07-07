import pandas as pd
import numpy as np
data=pd.read_csv("dataset/titanic-dataset.csv")
df=pd.DataFrame(data)

# print(df.columns)
# print(df.info())
# print(df.head(5))
# print(df.describe())
print(df["Survived"].value_counts())
print((df["Survived"]==1).sum())#number of people survived
print(
    f"Number of children: {(df['Age'] < 18).sum()} "
    f"and number of adults: {((df['Age'] >= 18) & (df['Age'] <= 40)).sum()} "
    f"and number of senior citizens: {(df['Age'] >= 60).sum()}"
)
print(df.columns)
print(df["Sex"].value_counts())