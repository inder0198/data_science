# from keras.models import Sequential
# from keras.layers import Dense
# from sklearn.model_selection import train_test_split
# import numpy
# # fix random seed for reproducibility
# numpy.random.seed(7)
#
# dataset = numpy.loadtxt("diabetes1.csv",delimiter=",")
#
# x=dataset[:,0:8]
# y=dataset[:,8]
#
# # print(x)
# # print(y)
#
# xtr,xts,ytr,yts = train_test_split(x,y,test_size=0.1,random_state=10)
#
# model = Sequential()
# model.add(Dense(12, input_dim=8, activation='relu')) #input layer
# model.add(Dense(8, activation='relu')) #interm layer
# model.add(Dense(1, activation='sigmoid')) #output layer
# # # Compile model
# model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# # # Fit the model
# model.fit(xtr, ytr, epochs=50, batch_size=10) #iteration
# # # evaluate the model
# scores = model.evaluate(x, y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
# # print(model.predict(Xts))
# from ann_visualizer.visualize import ann_viz
# ann_viz(model,title="Neural Network")



# ---------------------------------------------------------------------------------------------------------------------

def Merge(dict1, dict2):
    return (dict2.update(dict1))


# Driver code
dict1 = {'x': 1, 'y': 2, 'z':3}
dict2 = {'a': 4, 'b': 5, 'b':6}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)


# from collections import Counter
#
#
# def most_frequent(List):
#     occurence_count = Counter(List)
#     return occurence_count.most_common(1)[0][0]
#
#
# List = ['sun','mon','tue','wed','thu','fri','sat','sun','mon','mon']
# print(most_frequent(List))