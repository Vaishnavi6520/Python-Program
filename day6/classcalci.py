class Calci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
obj=Calci
Calcutor=Calci()
print(Calcutor.add())
print(Calcutor.sub())
print(Calcutor.multi())
print(Calcutor.divide())
