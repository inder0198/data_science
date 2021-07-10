import urllib.request
import bs4 as bs
import requests
import pandas as pd


url1="https://www.indiatoday.in/latest-headlines"
data=requests.get(url1).text
sp=bs.BeautifulSoup(data,"lxml")


# print(data.prettify())

# print(headlines)
headlines=[]
description=[]

for i in range(10):
    url="https://www.indiatoday.in/latest-headlines"+"?page="+str(i)
    print(url)
    dt=requests.get(url).text
    data1 = sp.find('section', attrs={"id": "content"})
    h = data1.find_all("h2")
    d = data1.find_all("p")

    h.pop()
    for i in h:
        news = i['title']
        headlines.append(news)

    for i in d:
        desc=i.text
        description.append(desc)

a={'Headlines':headlines,'Description':description}
df = pd.DataFrame(a)
# print(df.to_string())
df.to_csv("scrap.csv",index=False)