# from typing import DefaultDict
class Car:
    color="black"
    brand="BMW"

    def findMileage(self,li,km):
        return km/li

myCar=Car()
a=input("Enter a color: ")
b=input("Enter a brand: ")

l=int(input("Enter litres: "))
k=int(input("Enter kilometers: "))
mileage=myCar.findMileage(l,k)
myCar.color=a
myCar.brand=b
print(myCar.color)
print(myCar.brand)
print(mileage)

# #printing default values using object
# DefaultCar=Car()
# print(DefaultCar.color)
# print(DefaultCar.brand)