import re,sys
try:
    studentheader=['name','rollno','admno','college','parentname','mobilenumber','emailid','sub1mark','sub2mark','sub3mark','sub4mark','sub5mark']
    # t=0 
    studentslist=[]         
    class Student:
        def __init__(self,name,rollno,admno,college,parentname,mobilenumber,emailid) :
            self.name=name
            self.rollno=rollno
            self.admno=admno
            self.college=college
            self.parentname=parentname
            self.mobilenumber=mobilenumber
            self.emailid=emailid
    class Marks(Student):
        def __init__(self,name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            self.sub1mark=sub1mark
            self.sub2mark=sub2mark
            self.sub3mark=sub3mark
            self.sub4mark=sub4mark
            self.sub5mark=sub5mark
    
            super().__init__(name,rollno,admno,college,parentname,mobilenumber,emailid)
        def add(self):
        
            dict1={'name':self.name,'rollno':self.rollno,'admno':self.admno,'college':self.college,'parentname':self.parentname,'mobilenumber':self.mobilenumber,'emailid':self.emailid,'sub1mark':self.sub1mark,'sub2mark':self.sub2mark,'sub3mark':self.sub3mark,'sub4mark':self.sub4mark,'sub5mark':self.sub5mark}
            studentslist.append(dict1)
        
        def search(self,rollno):
            for i in studentslist:
                if str(i['rollno'])==str(rollno):
                    print(i)
        def display(self):
            print(studentslist)
        def ranking(self):
            for i in range(len(studentslist)):
                for j in range(0,len(studentslist)-i-1):
                    a=studentslist[j]
                    sum1=int(a['sub1mark'])+int(a['sub2mark'])+int(a['sub3mark'])+int(a['sub4mark'])+int(a['sub5mark'])
                    b=studentslist[j+1]
                    sum2=int(b['sub1mark'])+int(b['sub2mark'])+int(b['sub3mark'])+int(b['sub4mark'])+int(b['sub5mark'])
    
                    if sum1<sum2:
                        studentslist[j],studentslist[j+1]=studentslist[j+1],studentslist[j]
            for i in studentslist:
                a=i
                sum1=int(a['sub1mark'])+int(a['sub2mark'])+int(a['sub3mark'])+int(a['sub4mark'])+int(a['sub5mark'])
                print(i,sum1)
    
        def validation(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
            validation=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',name)
            validation1=re.match('^[1-9]',rollno)
            validation2=re.match('^[1-9]',admno)
            validation3=re.match(r'/([A-Z][^\s,.]+[.]?\s[(]?)*(University|Institute|College)[^,\d]*(?=,|\d)/',college)
            validation4=re.match(r'([a-zA-Z])\D*([a-zA-Z])$',parentname)
            validation5=re.match("(0|91)?[7-9][0-9]{9}",mobilenumber)
            validation6=re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',emailid)
            validation7=re.match('^[0-9]',sub1mark)
            validation8=re.match('^[0-9]',sub2mark)
            validation9=re.match('^[0-9]',sub3mark)
            validation10=re.match('^[0-9]',sub4mark)
            validation11=re.match('^[0-9]',sub5mark)
            if validation and validation1 and validation2 and validation3 and validation4 and validation5 and validation6 and validation7 and validation8 and validation9 and validation10 and validation11 and validation11:
                return [int(name),int(rollno),int(admno),int(college),int(parentname),int(mobilenumber),int(emailid),int(sub1mark),int(sub2mark),int(sub3mark),int(sub4mark),int(sub5mark)]
            else:
                print("you had enter wrong input")
                sys.exit()
                # return True
        obj=studentslist()
        while(True):
            print("1. Add student details - ")
            print("2. Display student details Like API - ")
            print("3. Search student by Rollno - ")
            print("4. Ranking - ")
            print("5. Exit - ")
            choice = int(input('enter your choice : '))
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
                obj.student(name,rollno,admno,college,parentname,mobilenumber,emailid,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark)
            if choice==2:
                print(studentslist)
            if choice==3:
                srollno = int(input('enter the rollno to search - '))
                print(list(filter(lambda i:i['rollno']==srollno,studentslist)))
            if choice == 4:
                print(sorted(studentslist,reverse=True,key=lambda i:i['total']))
            if choice==5:
                sys. exit()
except Exception:
    print("something went wrong")
finally:
    print("Thank you!!")
