# from keras.models import Sequential #model create
# from keras.layers import Dense #layers NN
# from sklearn.model_selection import train_test_split #data division
# import numpy #
# import pandas as pd
# # fix random seed for reproducibility
# numpy.random.seed(7)
# # load diabetes dataset
# dataset = pd.read_csv("train1.csv",usecols=['Survived','Pclass','Sex','Age']).dropna()
# gender = {'male': 1,'female': 0}
# dataset.Sex = [gender[item] for item in dataset.Sex]
# # split into input (X) and output (Y) variables
# X = dataset[['Pclass','Sex','Age']] # independent variable
# Y = dataset['Survived'] #dependent variable   Y~X
# Xtr,Xts,ytr,yts=train_test_split(X,Y,test_size=0.1,random_state=10) #90% train 10% test
# # # create model
# model = Sequential() #linear model
# model.add(Dense(12, input_dim=3, activation='relu')) #input layer
# model.add(Dense(8, activation='relu')) #interm layer
# model.add(Dense(1, activation='sigmoid')) #output layer
# # # Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # # Fit the model
# model.fit(Xtr, ytr, epochs=150, batch_size=10) #iteration
# # # evaluate the model
# scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# # print(model.predict(Xts))
# from ann_visualizer.visualize import ann_viz
# ann_viz(model,title="Neural network")


# ----------------------------------------------------------------------------------------------------------------------

from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
import numpy
# fix random seed for reproducibility
numpy.random.seed(7)

dataset = numpy.loadtxt("rh.csv",delimiter=",")

x=dataset[:,0:13]
y=dataset[:,13]

# print(x)
# print(y)

xtr,xts,ytr,yts = train_test_split(x,y,test_size=0.1,random_state=10)

model = Sequential()
model.add(Dense(12, input_dim=13, activation='relu')) #input layer
model.add(Dense(16, activation='relu')) #interm layer
model.add(Dense(8, activation='relu')) #interm layer
model.add(Dense(4, activation='relu')) #interm layer
model.add(Dense(2, activation='relu')) #interm layer
model.add(Dense(1, activation='sigmoid')) #output layer
# # Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # Fit the model
model.fit(xtr, ytr, epochs=150, batch_size=10) #iteration
# # evaluate the model
scores = model.evaluate(x, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# print(model.predict(Xts))
from ann_visualizer.visualize import ann_viz
ann_viz(model,title="Neural Network")

# ----------------------------------------------------------------------------------------------------------------------
# import pandas as pd
#
# read_file = pd.read_csv (r'C:\Users\Inderjeet\PycharmProjects\data_science\reprocessed.hungarian.data',delimiter=" " ,header = None)
# read_file.to_csv (r'C:\Users\Inderjeet\PycharmProjects\data_science\rh.csv', index=None)



