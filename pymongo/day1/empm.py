import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase= client['EmployeeDb']
Collection_name =mydatabase['Employee']
list=[]
class BookDetails:
    def addbookdetails(self,name,Address,phonenumber,designation,Company_name,Salary):
        dict1={"Empname":name,"Address":Address,"phonenumber":phonenumber,"designation":designation,"Company_name":Company_name,"Salary":Salary,}
        list.append(dict1)
obj1=BookDetails()
while(True):
    
    print("1.Add employee")
    print('2.View emp')
    print('3.Search employee')
    choice=int(input("enter your choice:"))
    if choice==1:
        name=input("enter the name - ")
        Address=input("enter the Address - ")
        phonenumber=input("enter the phonenumber - ")
        designation=input("enter the designation - ")
        Company_name=input("enter the company name - ")
        Salary=int(input('enter Salary '))
        obj1.addbookdetails(name,Address,phonenumber,designation,Company_name,Salary)
    if choice==2:
        print(list)
        break
    if choice==3:
        Collection_name = mydatabase['stu']
        result=Collection_name.delete_count
        print(result.deleted_count)
        list=[]
        for i in result:
            list.append(i)
result = Collection_name.insert_many(list)
print(result.inserted_ids)