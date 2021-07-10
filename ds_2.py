import pandas as pd
from tabulate import tabulate
data = pd.read_json("Sample Json with 200 Records.json")
r = []
for i in range(len(data)):
    temp = []
    df = data.loc[i]
    d = df[0]
    id = d["id"]
    name = d["name"]
    title = d["title"]
    description = d["description"]
    location = d["location"]
    temp = [id, name,description, title, location]
    r.append(temp)
df1 = pd.DataFrame(r, columns=["id", "name","description", "title", "location"])

print(tabulate(df1, headers=["id", "name","description", "title", "location"], tablefmt='psql'))