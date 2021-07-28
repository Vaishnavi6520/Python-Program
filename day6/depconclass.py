class Dept:
    def __init__(self,deptname):
        pass
    def addStudent(self,sname,sroll,sadmin,saddr):
        ob=Student(sname,sroll,sadmin,saddr)
        ls.append(ob)
    def displayStudent(self,ob):
        print("sname :",ob.sname)
        print("sroll :",ob.sroll)
        print("sadmin :",ob.sadmin)
        print("saddr :",ob.saddr)
        print("\n")

