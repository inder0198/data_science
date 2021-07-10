# import urllib.request
# import bs4 as bs
# import requests
# import pandas as pd
#
# url1 = urllib.request.urlopen("https://www.tiobe.com/tiobe-index/")
# sp = bs.BeautifulSoup(url1,"lxml")
# d = []
# table = sp.find ('table', attrs={'id':"top20",'id':"otherPL",'id':"VLTH",'id':"PLHoF"})
# fetch_row = table.find_all("tr")
# print(fetch_row)
#
# yt=[]
# for i in fetch_row:
#     tf = i.find_all('td')
#     tf1=[i.text for i in tf]
#     yt.append(tf1)
#
#
# # df = pd.DataFrame(yt,columns=["May 2021","May 2020","Change","Programming Language","Ratings","Change"])
# # df = pd.DataFrame(yt,columns=["Position","Programming Language","Ratings"])
# # df = pd.DataFrame(yt,columns=["Programming Language","2021","2016","2011","2006","2001","1996","1991","1986"])
# df = pd.DataFrame(yt,columns=["Year","Ratings"])
# df.dropna(inplace=True)
# print(df)
#
# df.to_excel("ttt5.xlsx",index=False)


# --------------------------------------------------------------------------------------------------------------------

import urllib

import requests
import bs4 as bs
import pandas as pd
import xlsxwriter

url = requests.get("https://www.tiobe.com/tiobe-index/").text
data = bs.BeautifulSoup(url, "lxml")
# print(data.prettify())
# table = data.find_all('table')
# table = data.find('table')
table1 = data.find("table", attrs={"id": "top20"})
table2 = data.find("table", attrs={"id": "otherPL"})
table3 = data.find("table", attrs={"id": "VLTH"})
table4 = data.find("table", attrs={"id": "PLHoF"})

a = []
tddata1 = []
tddata2 = []
tddata3 = []
tddata4 = []
for i in [table1, table2, table3, table4]:
    tr = i.find_all('tr')
    for j in tr:
        td = j.find_all('td')
        temp = [i.text for i in td]
        if i == table1:
            tddata1.append(temp)
        if i == table2:
            tddata2.append(temp)
        if i == table3:
            tddata3.append(temp)
        if i == table4:
            tddata4.append(temp)

del tddata1[0]
del tddata2[0]
del tddata3[0]
del tddata4[0]
# print(tddata1)

writer = pd.ExcelWriter('scrap1.xlsx', engine='xlsxwriter')

df1 = pd.DataFrame(tddata1,columns=["May 2021","May 2020","Change","Programming Language","Ratings","Change"])
df1.to_excel(writer, sheet_name='Sheet1', index=False)

df2 = pd.DataFrame(tddata2,columns=["Position","Programming Language","Ratings"])
df2.to_excel(writer, sheet_name='Sheet2',index=False)

df3 = pd.DataFrame(tddata3,columns=["Programming Language","2021","2016","2011","2006","2001","1996","1991","1986"])
df3.to_excel(writer, sheet_name='Sheet3',index=False)

df4 = pd.DataFrame(tddata4,columns=["Year","Winner"])
df4.to_excel(writer, sheet_name='Sheet4',index=False)

writer.save()