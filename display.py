import re,sys
# try:
header=['name','rollno','admno','college','parentname','mobilenumber','emailid','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark']
studentlist=[]
class Studentdetail:
    def addStudent(self,ls):
        self.name=ls[0]
        self.rollno=ls[1]
        self.admno=ls[2]
        self.college=ls[3]
        self.parentname=ls[4]
        self.mobilenumber=ls[5]
        self.emailid=ls[6]
class Marks(Studentdetail):
    def mark (self,ls):
        super()._init_(ls)
        self.sub1mark=ls[7]
        self.sub2mark=ls[8]
        self.sub3mark=ls[9]
        self.sub4mark=ls[10]
        self.sub5mark=ls[11]
    def addStudentdetail(self,name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        total=sub1mark+sub2mark+sub3mark+sub3mark+sub4mark+sub5mark
        dict={"name":name,"rollno":rollno,"admno":admno,"college":college,"parentname":parentname,"mobilenumber":mobilenumber,"emailid":emailid,"sub1mak":sub1mark,"sub2mark":sub2mark,"sub3mark":sub3mark,"sub4mark":sub4mark,"sub5mark":sub5mark}
        studentlist.append(dict)
    def validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        validation=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',name)
        validation1=re.match('^[1-9]',rollno)
        validation2=re.match('^[1-9]',admno)
        validation3=re.match(r'/([A-Z][^\s,.]+[.]?\s[(]?)(University|Institute|College)[^,\d](?=,|\d)/',college)
        validation4=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',parentname)
        validation5=re.match("(0|91)?[7-9][0-9]{9}",mobilenumber)
        validation6=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailid)
        validation7=re.match('^[0-3]{1}[0-9]{1}|40$',sub1mark)
        validation8=re.match('^[0-3]{1}[0-9]{1}|40$',sub2mark)
        validation9=re.match('^[0-3]{1}[0-9]{1}|40$',sub3mark)
        validation10=re.match('^[0-3]{1}[0-9]{1}|40$',sub4mark)
        validation11=re.match('^[0-3]{1}[0-9]{1}|40$',sub5mark)
        if validation and validation1 and validation2 and validation3 and validation4 and validation5 and validation6 and validation7 and validation8 and validation9 and validation10 and validation11 and validation11:
            return [int(name),int(rollno),int(admno),int(college),int(parentname),int(mobilenumber),int(emailid),int(sub1mark),int(sub2mark),int(sub3mark),int(sub4mark),int(sub5mark)]
        else:
            print("you had enter wrong input")
            sys.exit()
    obj=Studentdetail()
    while(True):
        print("1. Add Students -")
        print("2. Display student details Like API - ")
        print("3. Search student by Rollno - ")
        print("4. Ranking - ")
        print("5. Exit - ")
        choice=int(input("Enter your choice :"))
        if choice==1:
            name = input("enter the name of student : ")
            rollno=input("enter the Rollno : ")
            admno=input('enter the admin no :  ')
            college=input("enter the college name : ")
            parentname=input("enter the parent name : ")
            mobilenumber=input("enter the mobile number: ")
            emailid=input("enter the email id : ")
            sub1mark=input("enter the subject1 mark: ")
            sub2mark=input("enter the subject2 mark: ")
            sub3mark=input("enter the subject3 mark: ")
            sub4mark=input("enter the subject4 mark: ")
            sub5mark=input("enter the subject5 mark: ")
            obj=Studentdetail(validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark))
        if choice==2:
            print(studentlist)
        if choice==3:
            searchroll=int(input("Enter roll number to search :"))
            print(list(filter(lambda i:i["rollnum"]==searchroll,studentlist)))
        if choice==4:
            print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
        if choice==5:
            break
# except Exception:
#     print("Wrong input")
# finally:
#     print("Thank You!")