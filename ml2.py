# urllib - link read
# request - link text

import urllib.request
import bs4 as bs
import requests
import pandas as pd

# this opens wesite used for secured websites
# url1=urllib.request.urlopen("https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm").read()
#
# print(url1)
#
# sp=bs.BeautifulSoup(url1,"lxml")
# print(sp)

# this method is used to request and get the data from the website -
# url1="https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_installation.htm"
# l_t=requests.get(url1).text
#
# sp=bs.BeautifulSoup(l_t,"lxml")
# print(sp.prettify())

# to fetch table from a website
# url1=urllib.request.urlopen("https://www.w3schools.com/html/html_tables.asp").read()
#
# sp=bs.BeautifulSoup(url1,"lxml")
# dta=[]
# tabel=sp.find('table').prettify()
# print(tabel)
# fetch_row=tabel.find_all("tr")
# print(fetch_row)
#
# for i in fetch_row:
#     td=i.find_all('td')
#     data=[i.text for i in td]
#     print(data)



# url1 = urllib.request.urlopen("https://www.w3schools.com/html/html_tables.asp")
# sp = bs.BeautifulSoup(url1,"lxml")
# d = []
# table = sp.find('table')
# fetch_row = table.find_all("tr")
# print(fetch_row)
# for i in fetch_row:
#     tf = i.find_all('td')
#     print(tf)


url1 = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/")
sp = bs.BeautifulSoup(url1,"lxml")
d = []
table = sp.find('table')
fetch_row = table.find_all("tr")
print(fetch_row)

yt=[]
for i in fetch_row:
    tf = i.find_all('td')
    tf1=[i.text for i in tf]
    yt.append(tf1)


df = pd.DataFrame(yt,columns=["program names","internal points","kittens"])
df.dropna(inplace=True)
print(df)

df.to_excel("scr.xlsx",index=False)


# n = int(input("enter n:"))
# for i in range(n):
#     if i == 0:
#         b = 1
#         print(b)
#     else:
#         b += 4 * i
#         print(b)
