# import pandas as pd
#
# df = pd.read_csv("insurance.csv",usecols=['age', 'sex', 'bmi', 'children','smoker','charges']).dropna()
#
# gender = {'male': 1,'female': 0}
# df.sex = [gender[item] for item in df.sex]
#
# smoke = {'yes':1,'no':0}
# df.smoker = [smoke[item] for item in df.smoker]
# print(df)
#
# from sklearn import linear_model
#
# x = df[["age","sex","bmi","children","smoker"]]
# y = df["charges"]
#
# mod1 = linear_model.LinearRegression()
# mod1.fit(x, y)
#
# testdata = [[60,1,28.595,0,0]]
# p = mod1.predict(testdata)
# print(p)
#
# print(mod1.score(x,y))

# ----------------------------------------------------------------------------------------------------------------------

# import pandas as pd
# df = pd.read_excel("addm.xlsx")
# print(df)
#
# from sklearn import linear_model
# import numpy as np
#
# x = np.array(df["percentage"]).reshape(-1,1)
# y = df["addmision"]
#
# mod1 = linear_model.LogisticRegression()
# mod1.fit(x, y)
#
# testdata = pd.DataFrame({'percentage':[98,66,54,34,87,98]})
# p = mod1.predict(testdata)
# print(p)

# ----------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# df = pd.read_csv("insurance.csv",usecols=['age', 'sex', 'bmi', 'smoker']).dropna()
#
# gender = {'male': 1,'female': 0}
# df.sex = [gender[item] for item in df.sex]
#
# smoke = {'yes':1,'no':0}
# df.smoker = [smoke[item] for item in df.smoker]
# print(df.to_string())
#
# from sklearn import linear_model
#
# x = df[["age","sex","bmi"]]
# y = df["smoker"]
#
# mod1 = linear_model.LogisticRegression()
# mod1.fit(x, y)
#
# testdata = [[19,0,21.700]]
# p = mod1.predict(testdata)
# print(p)
#
# print(mod1.score(x,y))

# ----------------------------------------------------------------------------------------------------------------------

# import pandas as pd
#
# df = pd.read_csv("trainsurvive.csv",usecols=['Age', 'Sex', 'Pclass', 'Survived']).dropna()
#
# gender = {'male': 1,'female': 0}
# df.Sex = [gender[item] for item in df.Sex]
#
# print(df)
#
# from sklearn import linear_model
#
# x = df[["Age","Sex","Pclass"]]
# y = df["Survived"]
#
# mod1 = linear_model.LogisticRegression()
# mod1.fit(x, y)
#
# testdata = [[1,0,3]]
# p = mod1.predict(testdata)
# print(p)
#
# print(mod1.score(x,y))


# ----------------------------------------------------------------------------------------------------------------------

from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(list(iris.keys()))
# print(iris['data'].shape)
# print(iris['target'])
# print(iris['DESCR'])

X = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(np.int)

# Train a logistic regression classifier
clf = LogisticRegression()
clf.fit(X,y)
example = clf.predict(([[2.6]]))
print(example)

# Using matplotlib to plot the visualization
X_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(X_new)
print(y_prob)
plt.plot(X_new, y_prob[:,1], "g-", label="virginica")
plt.show()


# print(y)
# print(iris["data"])
# print(X)
