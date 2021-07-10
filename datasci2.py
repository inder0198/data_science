#data science
"""
#numpy mathamatical/statical
#pandas file handling/file mapulating(data collection/clean)
#matplotlib data vizulation
#sklearn/sci-kit module ML #data divided ML models (train & test)
#web scrapping beautifulsoup
"""
#numpy
#matrix operation
#1D
# import numpy as ny
# arr1=ny.array([3,4,1]) #1x3
# arr2=ny.array([7,9,2])
# #2D
# ar1=ny.array([(4,5,2),(6,7,3),(4,5,7)],dtype=int) #12+5+4=21
# ar2=ny.array(([(3,2,3),(5,2,1),(1,4,2)]))
# print(ar1+ar2)
# print(ar1-ar2)
# print(ar1.dot(ar2))
# print(ar1/ar2)
# print(ar2)
#reshape method
# print(ar1)
# testm=ny.array([(3,5,1,3),(5,6,2,1)],dtype=int)
# print(testm)
# print(testm.reshape(testm.shape[1],testm.shape[0])) #or reshape(2,4)
# print(testm.T)
#create or generate matrix using
#zeros
# cm=ny.zeros(3,dtype=int) #1D matrix
# print(cm)
# cm1=ny.zeros((3,3),dtype=int)
# print(cm1)
#full
# fm=ny.full((3,3),7)
# print(fm)
#eye
# em=ny.eye(4,dtype=int)
# print(em)
#ones
# n1=ny.ones((4,4),dtype=int)
# print(n1.shape)
# print(n1.size)
# print(n1.dtype)
#sort
# testm=ny.array([(10,3,1),(4,7,5),(7,9,8)],dtype=int)
# print(testm)
# testm.sort(axis=1) #0 means col wise sort #1 row wise sort
# print(testm)

#23/5/21

#operations:-
#add element or value in array:-(append,insert)
import numpy as np

# arr12=np.array([1,2,3,4,5,6,7,8,9],dtype=int)
# print(arr12)
# arr12=np.append(arr12,105)#(array_name,values)
# print(arr12)
# arr12=np.append(arr12,99)
# print(arr12)
#insert(array_name,index_postion,value)
# arr12=np.insert(arr12,0,33)
# print(arr12)
# arr12=np.insert(arr12,3,77)
# print(arr12)
# arr12=np.append(arr12,[[3,2,1]],axis=0)
# print(arr12)
# arr12=np.append(arr12,[[2],[4],[9]],axis=1)
# print(arr12)
#delete(array_name,index,axis 0/1)
# arr12=np.delete(arr12,0,1)
# print(arr12)
#splitting:-arrya_split/split(array_name,sub_data)
# arr12=np.split(arr12,3)
# print(arr12)
#indexing= access,modify
# print(arr12[3])# access
# arr12[3]=55 #modify /assign
# print(arr12)
# print(arr12[1,1])
# arr12[1,1]=55
# print(arr12)

# for j in range(10):
#     rarr=np.array([np.random.randint(1,100) for i in range(10)]) #list comprihension
#     rarr1=np.append(rarr,rarr,axis=0)
#10x10
# raaa=np.random.randint(100,size=20)#(range,size)
# print(raaa)
# ra1=np.random.randint(1000,size=(10,10))
# print(ra1)
#slicing :-data access
# print(raaa[3:9])
# print(ra1[4,5:10]) #fetch 4 row values
#print(ra1[5:10,4]) #fetch 4 col values
#aggregate_fucntion:-sum(),mean(),max(),min(),median()
# print(raaa.sum()/20)
# print(raaa.mean())
# print(ra1.max())

#pandas (modules):-file mapulating(dataframe,

#1)series
#2)data frame(table format data)
#3) 3d data


import numpy as np
import pandas as pd
# data=[np.random.randint(1,11) for i in range(10)]
# print(data)
# list into series
# sd=pd.Series(data)
# print(sd)

#dataframe:-
#basic form
# df1=pd.DataFrame([['id','name','cn_no'],[1001,'abc',9988998899],[1002,'xyz',9988998877]])
# print(df1)
#
# df2=pd.DataFrame({'id':[1001,1002,1003],"name":['abc','xyz','pqr'],"cn_no":[9999,8888,7777]})
# print(df2)
#
# df3=pd.DataFrame([[1001,'aaa'],[1002,'bbb'],[1003,'ccc']],columns=['id','name'])
# print(df3)
#read csv file using pandas and create dataframe?
data=pd.read_excel("Animal.xlsx")
# print(data.to_string())
# df1=pd.DataFrame(data)
# print(df1.to_string())

#read excel file?
# data=pd.read_excel('cars.xlsx')
# print(data)
#'mysql://root:root@localhost/demo12'
#read sql data using pandas
#sqlalchemy

# from sqlalchemy import create_engine #connection
# conn=create_engine('mysql://root:root@localhost/demo12') #connection object
# data=pd.read_sql('emp1',conn)
# print(data.to_string())

#read data from url + json

# url='https://api.exchangerate-api.com/v4/latest/USD'
# data=pd.read_json(url)
# print(data.to_string())
# data.to_excel("stockexchane.xlsx",header=True)
# data.to_csv("stockX.csv",header=True)
# print(df2)
# df2.to_sql("test",con=conn)
# df2.to_json("test.json")



#clean and visulizing
#matplotlib

#create data random emp_id or emp_name(8 char) generate 100 data store in excel file?
'''
emp_id     emp_name
1001       absjkdb

'''
# import random
# import string
# eid=[''.join(random.choices(string.digits,k=5)) for i in range(100)]
# name=[''.join(random.choices(string.ascii_uppercase,k=8)) for i in range(100)]
#
# import pandas as pd
# df11=pd.DataFrame({'name':name,"eid":eid})
# print(df11.to_string())
# df11.to_excel("randata.xlsx",index=False)
# import pandas as pd
# data=pd.read_excel("randata.xlsx")
# df1=pd.DataFrame(data)
# # print(df1)
# df1=df1.dropna()
# print(df1.to_string())


#vizulization:-
#line,scatter,bar,hist,pie
import matplotlib.pyplot as pl
# x=[3,6,9,12,14,17,20,22,26,30]
# y=[4,9,14,19,25,31,38,45,35,12]
# # pl.subplot(1,3,1)
# pl.subplot(2,1,1)
# pl.plot(x,y)
# # pl.plot(x,y,"*:y") #o,*,.,x,X,+,P,s,D,d,p,H,h,v,^,1,2,3,4,|,- /r,g,b,m,c,y,k,w
# # pl.plot(x,y,marker="*",ms=20,mec="r",c="r",mfc="y")
# # pl.plot(x,y,linestyle="solid",linewidth=1) #dotted,dashed,dashdot,solid
# f1={'family':"serif",'color':"red","size":20}
# f2={'size':15}
# pl.xlabel("X-axis",fontdict=f2)
# pl.ylabel("Y-axis",fontdict=f2)
# pl.title("Data",fontdict=f1)#,loc="right"
# pl.grid(color="red",linestyle="--",linewidth=1)#axis="x"
# x1=[3,5,8,11,19,25,31,40,47,52]
# y1=[5,11,19,27,35,42,50,59,33,20]
# # pl.subplot(1,3,3)
# pl.subplot(2,1,2)
# pl.plot(x1,y1)
# pl.show()

#scatter plot(point plot)

# import numpy as ny
# import random
#
# x=ny.array([random.randint(1,50) for i in range(50)])
# y=ny.array([random.randint(50,100) for i in range(50)])
# col=ny.array(['red','blue','green','yellow','pink','black','brown',"cyan","gray","purple",'red','blue','green','yellow','pink','black','brown',"cyan","gray","purple"])
# col=ny.array([i for i in range(1,101)])
# pl.scatter(x,y,c=col,cmap='Wistia')
# pl.colorbar()
# x1=ny.array([random.randint(1,50) for i in range(20)])
# y1=ny.array([random.randint(50,100) for i in range(20)])
# pl.scatter(x1,y1,color="black")
# sz=ny.array([random.randint(1,100)  for i in range(1,51)])
# pl.scatter(x,y,s=sz,alpha=0.5)
# pl.show()

#bar plot

# x=["A","B","C","D","E"]
# y=[20,40,10,40,50]
# col=['red','green','brown','yellow','cyan']
# pl.bar(x,y,color=col,width=0.6)
# pl.show()

#histogram plot

# y=[5,5,5,5,1,1,2,4,5,6,7,8,9,1,2,3,5,7,8,4,6,8,3,2,0,5,7,8,4,6,7,10]
# pl.hist(y)
# pl.show()

#pie plot

data=[33,56,12,90]
lb=['usa','japan','china','india']
col=['red','blue','yellow','green']
ex=[0,0,0,0.1]
pl.pie(data,labels=lb,explode=ex,shadow=True,colors=col)
pl.legend(title="country")
pl.show()

