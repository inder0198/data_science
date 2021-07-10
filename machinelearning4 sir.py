#SVM(support vector machine) classfication
# from sklearn import datasets
# data=datasets.load_iris()
#
# X=data.data#(sl,sw,pl,pw)
# y=data.target #species
#
# from sklearn.model_selection import train_test_split
# X_tr,X_ts,y_tr,y_ts=train_test_split(X,y,test_size=0.1,random_state=10) #90 train #10 test
#
# from sklearn.svm import SVC
# mod1=SVC(kernel="linear",C=1.0) #linear ,rbf(gussian)(gamma=0.0-1.0),ploy degree=0-50
# mod1.fit(X_tr,y_tr)
# print(y_ts)
# p=mod1.predict(X_ts)
# print(p)
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p))
#Animal classification
#50 data svm ,dt,rf
#ah    aw    fs   at
#5      3    3    dog
#3      2    1     cat


#furit class
#wight    color     firut
#50       red        apple
#80       orange     orange
#40       yellow     banana


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

