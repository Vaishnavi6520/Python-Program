import csv,json
myfile='petrol.csv'
jsonfilePath='petrol.json'
petrol_list=[]
#convert csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.DictReader(f)
    for data in dataReader:
        petrol_list.append(data)

petrol_list_json=json.dumps(petrol_list)
with open(jsonfilePath,'w+',encoding='utf-8') as f:
    f.write(petrol_list_json)
