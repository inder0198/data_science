import string
import random
import pandas as p

a = 1001
data1 = [['id', 'name', 'salary']]
for i in range(10):
    temp = []
    a += i
    b = ran = ''.join(random.choices(string.ascii_lowercase, k=5))
    c = random.randint(20000, 30000)
    temp.append(a)
    temp.append(b)
    temp.append(c)

    data1.append(temp)

df = p.DataFrame(data1)
print(df)