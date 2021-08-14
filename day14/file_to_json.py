import csv,json
myfile='product.csv'
jsonfilePath='product.json'
product_list=[]
#convert csv to list
with open(myfile,'r',encoding='utf-8') as f:
    dataReader=csv.reader(f)
    for data in dataReader:
        product_list.append(data)

product_list_json=json.dumps(product_list)
with open(jsonfilePath,'w',encoding='utf-8') as f:
    f.write(product_list_json)
