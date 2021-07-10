# from sklearn.tree import DecisionTreeClassifier #(gini)
# import pandas as pd
# data=pd.read_csv('diabetes.csv')
# X=data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
# y=data['Outcome']
# from sklearn.model_selection import train_test_split
# X_tr,X_ts,y_tr,y_ts=train_test_split(X,y,test_size=0.1,random_state=10)
# mod1=DecisionTreeClassifier(criterion="entropy",max_depth=6)
# mod1.fit(X_tr,y_tr)
# p1=mod1.predict(X_ts)
# # print(y_ts)
# print(p1)
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p1))

# ----------------------------------------------------------------------------------------------------------------------

# from sklearn import datasets
# data = datasets.load_iris()
#
# x=data.data
# y=data.target
#
# from sklearn.model_selection import train_test_split
# x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.4,random_state=10) # 90 train data 10 test data
#
# from sklearn.tree import DecisionTreeClassifier
# mod1=DecisionTreeClassifier(criterion="entropy",max_depth=5)
# mod1.fit(x_tr,y_tr)
# print(y_ts)
# p=mod1.predict(x_ts)
# print(p)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p))

# ----------------------------------------------------------------------------------------------------------------------

# from sklearn.ensemble import RandomForestClassifier
# import pandas as pd
# data=pd.read_csv('diabetes.csv')
# X=data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
# y=data['Outcome']
# from sklearn.model_selection import train_test_split
# X_tr,X_ts,y_tr,y_ts=train_test_split(X,y,test_size=0.1,random_state=10)
# mod1=RandomForestClassifier(n_estimators=100)
# mod1.fit(X_tr,y_tr)
# p1=mod1.predict(X_ts)
# # print(y_ts)
# print(p1)
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p1))

# ----------------------------------------------------------------------------------------------------------------------

from sklearn import datasets
data = datasets.load_iris()

x=data.data
y=data.target

from sklearn.model_selection import train_test_split
x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.3,random_state=10) # 90 train data 10 test data

from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

mod11=SVC(kernel="linear",C=1.0)
mod12=SVC(kernel="poly",degree=20)
mod13=SVC(kernel="rbf",gamma=0.4)
mod11.fit(x_tr,y_tr)
mod12.fit(x_tr,y_tr)
mod13.fit(x_tr,y_tr)
p11=mod11.predict(x_ts)
p12=mod12.predict(x_ts)
p13=mod13.predict(x_ts)
# print(y_ts)
print(p11)
print(p12)
print(p13)

mod2=DecisionTreeClassifier()
mod2.fit(x_tr,y_tr)
print(y_ts)
p2=mod2.predict(x_ts)
print(p2)

mod3=RandomForestClassifier(n_estimators=100)
mod3.fit(x_tr,y_tr)
print(y_ts)
p3=mod3.predict(x_ts)
print(p3)

from sklearn import metrics
print(metrics.accuracy_score(y_ts,p11))
print(metrics.accuracy_score(y_ts,p12))
print(metrics.accuracy_score(y_ts,p13))
print(metrics.accuracy_score(y_ts,p2))
print(metrics.accuracy_score(y_ts,p3))

