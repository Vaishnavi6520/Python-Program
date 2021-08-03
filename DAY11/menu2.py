import collections
import re
print("Select an option from menu :")
print("\n")
print("1. Add_Employee")
print("2. View_Employee")
choice=int(input("Enter the choice"))
li=[]
if(choice==1):
    for i in range(2):
        dict={}
        print("Add_Employee details")
        dict["name"]=input("Enter the Employee Name :")
        dict["id"]=input("Enter the ID :")
        dict["designation"]=input("Enter the Designation :")
        salary=input("Enter the salary :")
        amount=re.search("^[0-9]",salary)
        if amount:
            dict['salary']=salary
        dict["address"]=input("Enter the address :")
        phone=input("Enter the phone no. :")
        validation_number=re.search("^[6-9]\d{9}$",phone)
        if validation_number:
            dict["phone"]=phone
        pincode=input("Enter the pincode :")
        validation_pincode=re.search("^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",pincode)
        if validation_pincode:
            dict["pincode"]=pincode
        li.append(dict)
    c=int(input("2. View Employee"))
    if(c==2):
        print("View employee is selected :")
        for i in range(len(li)-1):
            combi_dict=collections.ChainMap(li[i],li[i+1])
            print(combi_dict)
else:
    print("Wrong choice")

