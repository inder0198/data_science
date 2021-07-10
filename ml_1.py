#sklearn, tensorflow, keras
# machine learning models (supervised, unsupervised),data split, normalise/standarised,cross validation(model accuracy)

from sklearn import datasets
from sklearn import svm

data1=datasets.load_iris()#flower data leaves
data2=datasets.load_diabetes()
print(data2)

# print(data1.feature_names)
# print(data1.target_names)

#data split (train and test)
from sklearn.model_selection import train_test_split

x=data1.data#independent data(given data or input data)feature
y=data1.target#dependent data(output data)label
print(x.shape,y.shape)
# (y~x) formula x is given to find y output
#random state to randomly select data for training and testing in ratio to the test_size(jitna % training data hai utna hi use hoga)
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=1)# 70% data for training and 30% for testing

mod1=svm.SVC(kernel="linear")
mod1.fit(x_train,y_train)
print(y_test)
print(mod1.predict(x_test))
print(mod1.score(x_test,y_test))

from sklearn.model_selection import cross_val_score

sco=cross_val_score(mod1,x,y,cv=5)
print(sco)
print(sco.mean(),sco.std())

# print(x_train.shape,x_test.shape)
# print(y_train.shape,y_test.shape)

#normalization/standardisation (-1,1) converts the data in range of -1 to 1
# formula: x-x min/x max -x min

# from sklearn import preprocessing
# import numpy as np
# input_data = np.array([
#                       [2.1,-1.9,5.5],
#                       [-1.5,2.4,3.5],
#                       [0.5,-7.9,5.6],
#                       [5.9,2.3,-5.8]
#                       ])
#
# data_normalised_l1 = preprocessing.normalize(input_data,norm='l1')
# print("\nL1 normalised data:\n",data_normalised_l1)
#
# data_normalised_l2 = preprocessing.normalize(input_data,norm='l2')
# print("\nL2 normalised data:\n",data_normalised_l2)


