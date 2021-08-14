import requests
import json
data=requests.get("https://jsonplaceholder.typicode.com/posts")
edata=data.json()
p=[]
for i in edata:
    p.append(i)["title"]

lis=[x for x in p if x[0]=='a' in x]
print(lis)