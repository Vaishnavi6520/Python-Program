class AdditionOperation:
    def addTwoNum(self,a,b):
        return a+b
class SubtractOperation:
    def subTwoNum(self,a,b):
        return a-b

class MultiOperation:
    def multiTwoNum(self,a,b):
        return a*b

class Calculator(AdditionOperation,SubtractOperation,MultiOperation):
    pass

objcalci=Calculator()
x=int(input("Enter a number : "))
y=int(input("Enter a number : "))
print(objcalci.multiTwoNum(x,y))
print(objcalci.addTwoNum(x,y))
print(objcalci.subTwoNum(x,y))

