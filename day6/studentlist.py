#list of object concept

class Student:
    def __init__(self,name,rollno,adminno):
        self.myname=name
        self.myrollno=rollno
        self.myadminno=adminno

obj=[]
obj.append(Student("Vaishnavi",101,1))
obj.append(Student("Vaishali",102,2))
obj.append(Student("Vaibhav",103,3))
print(obj[0].myname)
print(obj[1].myrollno)
print(obj[2].myadminno)

