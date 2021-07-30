import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/posts")
E=data.json()
articlesname=E["data"]
print(articlesname)
li=[]

li=[i for i in li if 'a' in i]
print(li)