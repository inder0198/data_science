import urllib.request
from bs4 import BeautifulSoup
import bs4 as bs
import pandas as pd
import requests

# html_page = urllib.request.urlopen("http://100photos.time.com/")
# soup = BeautifulSoup(html_page)
# images = []
# for img in soup.findAll('img'):
#     images.append(img.get('src'))
#     images.append(img.get('alt'))
# df = pd.DataFrame(images,columns=["Images Links"])
# df.to_excel("ttt6.xlsx",index=False)
# print(images)

url = requests.get("http://100photos.time.com").text
data = bs.BeautifulSoup(url, "lxml")
# print(data.prettify())
idata=data.find_all('img')
# print(idata)
a=[]
b=[]
for i in idata:
    # print(i)
    src=i['src']
    nm=i['alt']
    # print(src,nm)
    a.append(src)
    b.append(nm)
# print(a)
c={"Src":a,"Name":b}
print(c)
df=pd.DataFrame(c)
print(df)
df.to_excel("scrap3.xlsx",index=False)
x=pd.read_excel("scrap3.xlsx")
print(x.to_string())
