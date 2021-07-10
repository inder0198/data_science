# fetch data from mysql and create dataframe
# import pandas as pd
# import mysql.connector as my
# conn=my.connect(host="localhost",user="root",password="root",database="inder")
# cur=conn.cursor()
# q="select * from forms"
# cur.execute(q)
# r=cur.fetchall()
# df1=pd.DataFrame(r)
# print(df1)

# fetch data from url and create dataframe
# import pandas as pd
# df1=pd.read_csv("https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv")
# print(df1)


# first 5 data,last 5 data,size of row and column,information,description
# head(5),tail(5),shape(),info(),describe()
# import pandas as pd
# from tabulate import tabulate
# data = pd.read_json("Sample Json with 200 Records.json")
# r = []
# for i in range(len(data)):
#     temp = []
#     df = data.loc[i]
#     d = df[0]
#     id = d["id"]
#     name = d["name"]
#     title = d["title"]
#     description = d["description"]
#     location = d["location"]
#     temp = [id, name, title, location]
#     r.append(temp)
# df1 = pd.DataFrame(r, columns=["id", "name", "title", "location"])
# print(df1.head(10))
# print(df1.tail(10))
# print(df1.shape)
# print(df1.info())
# print(df1.describe())

# read data from excel sheet xlsx(install xlrd, openpyxl)
# import pandas as pd
# df1=pd.read_excel("Book1.xlsx")
# print(df1)


# write dataframe to xlxs and csv
# import pandas as pd
# import random
# df1=pd.DataFrame([random.randint(i,60)for i in range (30,60)],columns=["Age"])
# print(df1)
# df1.to_csv("test.csv",index=False)
# df1.to_excel("test.xlsx",index=False)
# df1.to_excel("test1.xls",index=False)


# write dataframe to sql
# import pandas as pd
# import random
# import sqlalchemy
# engine = sqlalchemy.create_engine('mysql://root:root@localhost/inder')
# df1=pd.DataFrame([random.randint(i,60)for i in range (30,60)],columns=["Age"])
# print(df1)
# df1.to_sql('emp_age',engine,if_exists='replace')


# create a dataframe of 100 datas and write to xls,csv,sql
# '''
# empid(1-100)    empname(5-12)   salary(30000-50000)
# '''
# import random
# import pandas as pd
# import string
# import sqlalchemy
# engine = sqlalchemy.create_engine('mysql://root:root@localhost/inder')
# a=random.randint(5,12)
# data1={"id":[i for i in range(1,101)],"name":[''.join(random.choices(string.ascii_lowercase, k=a)) for i in range(1,101)], "salary":[random.randint(30000, 50000) for i in range(1,101)]}
# df1=pd.DataFrame(data1)
# print(df1)
# df1.to_sql('emp_data',engine,if_exists='replace')
# df1.to_csv("test21.csv",index=False)
# df1.to_excel("test21.xlsx",index=False)
# df1.to_excel("test22.xls",index=False)




