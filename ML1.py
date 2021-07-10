import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("speed&dist.xlsx")
# print(df)

# create dependent(find or predict) and independent (input) variable formula:x~y x is dependent on y

# x = df["dist"] #independent
x = np.array(df["dist"]).reshape(-1,1)
y = df["speed"] #dependent

print(x,y)

# create models
from sklearn import linear_model

mod1= linear_model.LinearRegression()
mod1.fit(x,y) # model done
# predict the data
testdata = pd.DataFrame({'dist':[1000,40000,10,500]})
p = mod1.predict(testdata)
print(p)

print(mod1.score(x,y))

plt.scatter(x,y)
plt.plot(x,mod1.predict(x))
plt.show()