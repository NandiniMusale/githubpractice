import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\DELL\Downloads\wine+quality\winequality-red.csv",sep=";")
X=df.iloc[:,:-1]
Y=df["quality"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.33,random_state=42)
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_train_scaled=scaler.fit_transform(x_train)
x_test_scaled=scaler.transform(x_test)
#logistic regression
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train_scaled,y_train)
y_pred=model.predict(x_test_scaled)
from sklearn.metrics import accuracy_score
l_score=accuracy_score(y_pred,y_test)
print(l_score)
#support vector classifier
from sklearn.svm import SVC
svm_model=SVC()
svm_model.fit(x_train_scaled,y_train)
y_pred_svm=svm_model.predict(x_test_scaled)
from sklearn.metrics import accuracy_score
s_score=accuracy_score(y_pred_svm,y_test)
print(s_score)
#decision tree classifier
from sklearn.tree import DecisionTreeClassifier
dt_model=DecisionTreeClassifier()
dt_model.fit(x_train,y_train)
dt_pred=dt_model.predict(x_test)
from sklearn.metrics import accuracy_score
dt_score=accuracy_score(dt_pred,y_test)
print(dt_score)
#randomforest classifier
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier()
rf_model.fit(x_test,y_test)
rf_pred=rf_model.predict(x_test)
from sklearn.metrics import accuracy_score
rf_score=accuracy_score(rf_pred,y_test)
print(rf_score)

