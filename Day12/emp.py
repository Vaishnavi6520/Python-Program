import re
employee_list=[]
class EmpDetails:
    def AddEmp(self,id,name,designation,salary,address,phone,pincode):
        dict1={"id":id,"name":name,"designation":designation,"salary":salary,"address":address,"phone":phone,"pincode":pincode}
        employee_list.append(dict1)
obj1=EmpDetails()

def validation_emp(employee_name,employee_id):
    val=re.match("([a-z]+)([a-z]+)*([a-z]+)*$",employee_name)
    val2=re.match("[0-9]{0,7}$",employee_id)
    if val and val2:
        return True
    else:
        return False


while(1):
    print("1. Add Employee: ")
    print("2. View Employee: ")
    print("3. Exit: ")
    choice=int(input("Enter a choice: "))
    if choice==1:
        while(True):
            id=input("Enter id: ")
            name=input("Enter name: ")
            if validation_emp(name,id):
                designation=input("Enter designation: ")
                salary=input("Enter salary: ")
                address=input("Enter address: ")
                phone=input("Enter phone: ")
                pincode=input("Enter pincode: ")
                obj1.AddEmp(id,name,designation,salary,address,phone,pincode)
            else:
                print("Please enter valid names")
                continue
            break
    if choice==2:
        print(employee_list)
    if choice==3:
        break