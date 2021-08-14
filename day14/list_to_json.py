import json
studentlist=[{"name":"Anuj","roll":21},{"name":"Priya","roll":22}]
print(json.dumps(studentlist))
with open('test.json','w',encoding='utf-8') as f:
    f.write(myjsondata)