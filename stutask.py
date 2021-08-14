class Studentdeatils:
    student=[]
    def getData(self,name,rollno,admno,college,parentname,mobilenumber,emailid):
        Studentdeatils.name = name
        Studentdeatils.rollno = rollno
        Studentdeatils.admno = admno
        Studentdeatils.college = college
        Studentdeatils.parentname = parentname
        Studentdeatils.mobilenumber = mobilenumber
        Studentdeatils.emailid = emailid

    def displayData(self):
        print("Enter student name :",Studentdeatils.name)
        print("Enter student roll number :",Studentdeatils.rollno)
        print("Enter student admission number :",Studentdeatils.admno)
        print("Enter student college :",Studentdeatils.college)
        print("Enter student parent name :",Studentdeatils.parentname)
        print("Enter student mobile number :",Studentdeatils.mobilenumber)
        print("Enter student email id :",Studentdeatils.emailid)

class Sem1Result:
    semresult=[]
    def getData(self,sub1mark,sub2mark,sub3mark,sub4mark,sub5mark):
        Sem1Result.sub1mark=sub1mark
        Sem1Result.sub2mark=sub2mark
        Sem1Result.sub3mark=sub3mark
        Sem1Result.sub4mark=sub4mark
        Sem1Result.sub5mark=sub5mark
    def submark(self):
        print("Enter the Subject 1 marks :",Sem1Result.sub1mark)
        print("Enter the Subject 2 marks :",Sem1Result.sub2mark)
        print("Enter the Subject 3 marks :",Sem1Result.sub3mark)
        print("Enter the Subject 4 marks :",Sem1Result.sub4mark)
        print("Enter the Subject 5 marks :",Sem1Result.sub5mark)
    
