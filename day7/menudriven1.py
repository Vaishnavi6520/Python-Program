def Addition(num):
    return a+b
def subtraction(num):
    return a-b
def multiplication(num):
    return a*b
def division(num):
    return a/b
while(True):
    print("Select an option from menu ")
    print("\n")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=int(input("Enter the choice :"))
    if choice==1:
        print("Addition selected")
        a=int(input("Enter a  number :"))
        b=int(input("Enter a  number :"))
        print(Addition(a))
        break

    if choice==2:
        print("Subtraction selected")
        a=int(input("Enter a  number :"))
        b=int(input("Enter a  number :"))
        print(subtraction(a))
        break

    if choice==3:
        print("Multiplication selected")
        a=int(input("Enter a  number :"))
        b=int(input("Enter a  number :"))
        print(multiplication(a))
        break

    if choice==4:
        print("Division selected")
        a=int(input("Enter a  number :"))
        b=int(input("Enter a  number :"))
        print(division(a))
        break

    if choice==5:
        break
    else:
        print("Choose correct option")
    
