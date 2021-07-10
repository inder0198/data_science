# SVM (support vector machine) classification

# from sklearn import datasets
# data = datasets.load_iris()
#
# x=data.data
# y=data.target
#
# from sklearn.model_selection import train_test_split
# x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.1,random_state=10) # 90 train data 10 test data
#
# from sklearn.svm import SVC
# mod1=SVC(kernel="linear", C=1.0)
# mod1.fit(x_tr,y_tr)
# print(y_ts)
# p=mod1.predict(x_ts)
# print(p)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p))
#
# mod2=SVC(kernel="rbf")
# mod2.fit(x_tr,y_tr)
# print(y_ts)
# p=mod2.predict(x_ts)
# print(p)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p))
#
# mod3=SVC(kernel="poly")
# mod3.fit(x_tr,y_tr)
# print(y_ts)
# p=mod3.predict(x_ts)
# print(p)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p))

# ----------------------------------------------------------------------------------------------------------------------

# from sklearn import metrics
# from sklearn.svm import SVC
# import pandas as pd
# df = pd.read_csv("Iris.csv")
# x = df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]]
# y = df["Species"]
# mod2 = SVC(kernel="rbf")
# mod2.fit(x,y)
# e = mod2.predict(x)
# print(metrics.accuracy_score(y,e))
# print(mod2.score(x,y))

# ----------------------------------------------------------------------------------------------------------------------

# from sklearn.svm import SVC
# import pandas as pd
# df = pd.read_csv("dog&cat.csv")
# x = df[["ah","aw","fs"]]
# y = df["at"]
# from sklearn.model_selection import train_test_split
# x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.1,random_state=10) # 90 train data 10 test data
#
#
# mod1 = SVC(kernel="linear")
# mod2 = SVC(kernel="rbf")
# mod3 = SVC(kernel="poly")
#
# mod1.fit(x_tr,y_tr)
# mod2.fit(x_tr,y_tr)
# mod3.fit(x_tr,y_tr)
#
# print(y_ts)
# p1=mod1.predict(x_ts)
# p2=mod2.predict(x_ts)
# p3=mod3.predict(x_ts)
# print(p1,p2,p3)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p1))
# print(metrics.accuracy_score(y_ts,p2))
# print(metrics.accuracy_score(y_ts,p3))


# ----------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# data=pd.read_excel("Animal.xlsx")
# X=data[['animal_height','animal_width','face_skill ']]
# y=data['animal_type']
# from sklearn.model_selection import train_test_split
# X_tr,X_ts,y_tr,y_ts=train_test_split(X,y,test_size=0.1,random_state=10)
# from sklearn.svm import SVC
# mod1=SVC(kernel="linear",C=1.0)
# mod2=SVC(kernel="poly",degree=20)
# mod3=SVC(kernel="rbf",gamma=0.4)
# mod1.fit(X_tr,y_tr)
# mod2.fit(X_tr,y_tr)
# mod3.fit(X_tr,y_tr)
# p1=mod1.predict(X_ts)
# p2=mod2.predict(X_ts)
# p3=mod3.predict(X_ts)
# print(y_ts)
# print(p1)
# print(p2)
# print(p3)

# ----------------------------------------------------------------------------------------------------------------------


# import pandas as pd
# data=pd.read_csv('diabetes.csv')
# X=data[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
# y=data['Outcome']
# from sklearn.model_selection import train_test_split
# X_tr,X_ts,y_tr,y_ts=train_test_split(X,y,test_size=0.1,random_state=10)
# from sklearn.svm import SVC
# mod1=SVC(kernel="linear",C=1.0)
# # mod2=SVC(kernel="poly",degree=20)
# # mod3=SVC(kernel="rbf",gamma=0.4)
# mod1.fit(X_tr,y_tr)
# # mod2.fit(X_tr,y_tr)
# # mod3.fit(X_tr,y_tr)
# p1=mod1.predict(X_ts)
# # p2=mod2.predict(X_ts)
# # p3=mod3.predict(X_ts)
# # print(y_ts)
# print(p1)
# # print(p2)
# # print(p3)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p1))
# # print(metrics.accuracy_score(y_ts,p2))
# # print(metrics.accuracy_score(y_ts,p3))