import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

data=pd.read_csv("dataset/Titanic_train_dataset.csv")
df=pd.DataFrame(data)
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Fare"]=df["Fare"].fillna(df["Fare"].mean())
df["Cabin"]=df["Cabin"].fillna("Unknown")
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
print(df.isnull().sum())
print(df.columns)
le=LabelEncoder()
df["Sex"]=le.fit_transform(df["Sex"])
df["Embarked"]=le.fit_transform(df["Embarked"])
df["Cabin"]=le.fit_transform(df["Cabin"])
print(df.head(5))
X_drop=df.drop(["PassengerId","Name","Ticket","Survived"],axis=1)
y=df["Survived"]
X_train,X_test,y_train,y_test=train_test_split(X_drop,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred)
recall=recall_score(y_test,y_pred)
f1=f1_score(y_test,y_pred)
confusion=confusion_matrix(y_test,y_pred)
print(accuracy)
print(precision)
print(recall)
print(f1)
print(confusion)
print(model.score(X_train, y_train))
print(model.score(X_test, y_test))

