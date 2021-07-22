# reusable code
# function defines
# def sayHello():
#     # print("hello")
#     return "hello"
# # Function called
# x=sayHello()
# print(x)
# print(sayHello())
def sayHello(names):
    return "hello "+ names
getName=input("Enter name: ")
print(sayHello(getName))    