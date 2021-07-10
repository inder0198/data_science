# data cleaning
# 1. Empty cells (data)
# 2. Wrong data
# 3.Duplicate data


# # 1.Empty cells
# import pandas as pd
# # step 1
# df=pd.read_excel("book1.xlsx")
# print (df)
# # step 2 for new dataframe
# n_df=df.dropna()
# print(n_df)

# # 1.Empty cells
# import pandas as pd
# # step 1:
# df=pd.read_excel("book1.xlsx")
# print (df)
# step 2: remove nan for same dataframe
# df.dropna(inplace=True)
# print(df)
# # step 3: clean data Nan put some data
# df['roll'].fillna(10,inplace=True)
# print(df)
# df.dropna(subset=['class'],inplace=True)
# print(df)
# step 4: clean data replace data
# df.loc[6,'roll']=7
# print(df)
# step 5: clean data remove duplicates
# df.drop_duplicates(subset=['roll'],inplace=True)
# print(df)

# read specific column from csv file using usecols
# import pandas as pd
# data = pd.read_csv("heart.csv",usecols=['age', 'sex', 'trestbps', 'chol','thalach','oldpeak'])
# print(data)

# read specific column from csv file
# import pandas as pd
# from tabulate import tabulate
# data = pd.read_csv("heart.csv")
# print(data[['age', 'sex', 'trestbps', 'chol','thalach','oldpeak']])
# # delete those data where age is 55-60
# for x in data.index:
#   if 55 < data.loc[x, "age"] and data.loc[x, "age"] < 61:
#     data.drop(x, inplace = True)
# print((tabulate(data, headers=['age','sex','trestbps','chol','thalach','oldpeak'],tablefmt="fancy_grid")))


from tabulate import tabulate
import pandas as pd
data = pd.read_csv("heart.csv",usecols=['age', 'sex', 'trestbps', 'chol','thalach','oldpeak'])
print(data)
for x in data.index:
  if 55 < data.loc[x, "age"] and data.loc[x, "age"] < 61:
    data.drop(x, inplace = True)
print((tabulate(data, headers=['age','sex','trestbps','chol','thalach','oldpeak'],tablefmt="fancy_grid")))


