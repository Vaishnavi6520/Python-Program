class Person:
    def __init__(self,name):
        self.myname = name
    def sayMyName(self):
        print(self.myname)
n=input("Enter a name: ")
p=Person(n)
p.sayMyName()