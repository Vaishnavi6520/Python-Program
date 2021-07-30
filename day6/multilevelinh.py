class India:
    def alotNumber(self, number):
        print(number)

class CarManufacture(India):
    def makeACar(self,brand,color,price):
        print(brand,color,price)

class Seller(CarManufacture):
    def CustomerOrder(self,name,mobno):
        print(name,mobno)

objSeller=Seller()
objSeller.CustomerOrder("Vaishnavi",7865479754)
objSeller.makeACar("BMW","Black",20000000)
objSeller.alotNumber("MP12C28736")

all program today
for a inheritance or multilevel 3-4 example