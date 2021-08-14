import csv,json
myfile='diesel.csv'
jsonfilePath='diesel.json'
diesel_list=[]
#convert csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.reader(f)
    for data in dataReader:
        diesel_list.append(data)

diesel_list_json=json.dumps(diesel_list)
with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(diesel_list_json)
