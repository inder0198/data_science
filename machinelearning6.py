# from sklearn.neighbors import KNeighborsClassifier
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
# import numpy as np
#
# from sklearn import datasets
# data = datasets.load_iris()
#
# x = np.array(df["percentage"]).reshape(-1,1)
# x=['SepalLengthCm']
# y=['']
#
# # from sklearn.model_selection import train_test_split
# # x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.1,random_state=10) # 90 train data 10 test data
#
# mod1=KNeighborsClassifier(n_neighbors=10)
# mod1.fit(x,y)
# # p=mod1.predict(y)
# # print(p)
#
# # from sklearn import metrics
# # print(metrics.accuracy_score(y,p))
#
# plt.scatter(x,y)
# plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# df = pd.read_excel("addm.xlsx")
# print(df)
#
# import numpy as np
#
# x = np.array(df["percentage"]).reshape(-1,1)
# y = df["addmision"]
#
# mod1 = KNeighborsClassifier(n_neighbors=10)
# mod1.fit(x, y)
#
# testdata = pd.DataFrame({'percentage':[98,66,54,34,87,98]})
# p = mod1.predict(testdata)
# print(p)
#
# plt.scatter(x,y)
# plt.show()

# ----------------------------------------------------------------------------------------------------------------------
# from sklearn.neighbors import KNeighborsClassifier  # (for KNN)checks using points
#
# import pandas as pd
# df = pd.read_csv("iris.csv")
#
# Species = {'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica':2}
# df.Species = [Species[item] for item in df.Species]
#
# x = df[["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]].values
# y = df["Species"].values
# from sklearn.model_selection import train_test_split
# x_tr,x_ts,y_tr,y_ts = train_test_split(x,y,test_size=0.1,random_state=10)
# mod1 = KNeighborsClassifier(n_neighbors=10)
# mod1.fit(x_tr,y_tr)
# p1 = mod1.predict(x_ts)
# print(y_ts)
# print(p1)
#
# from sklearn import metrics
# print(metrics.accuracy_score(y_ts,p1))

# ----------------------------------------------------------------------------------------------------------------------

# import matplotlib
# matplotlib.use('GTKAgg')
#
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import ListedColormap
# from sklearn import neighbors, datasets
#
# n_neighbors = 6
#
# # import some data to play with
# iris = datasets.load_iris()
#
# # prepare data
# X = iris.data[:, :2]
# y = iris.target
# h = .02
#
# # Create color maps
# cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA','#00AAFF'])
# cmap_bold = ListedColormap(['#FF0000', '#00FF00','#00AAFF'])
#
# # we create an instance of Neighbours Classifier and fit the data.
# clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
# clf.fit(X, y)
#
# # calculate min, max and limits
# x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
# y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
# xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
# np.arange(y_min, y_max, h))
#
# # predict class using data and kNN classifier
# Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#
# # Put the result into a color plot
# Z = Z.reshape(xx.shape)
# plt.figure()
# plt.pcolormesh(xx, yy, Z, cmap=cmap_light)
#
# # Plot also the training points
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())
# plt.title("3-Class classification (k = %i)" % (n_neighbors))
# plt.show()
#
#

# ----------------------------------------------------------------------------------------------------------------------
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("iris.csv")
# print(df.to_string())

Species = {'Iris-setosa': 0,'Iris-versicolor': 1,'Iris-virginica':2}
df.Species = [Species[item] for item in df.Species]

x = df.iloc[:,[1,2,3,4]].values
# print(x)

kmean=KMeans(n_clusters=3)
km_p = kmean.fit_predict(x)
print(km_p)

plt.scatter(x[:,0],x[:,3],c=km_p,cmap="rainbow")
plt.show()


