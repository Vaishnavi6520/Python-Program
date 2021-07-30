class Employee:
    name="Raja"

    def printName(self):
        print(self.name)

Employee.printName=classmethod(Employee.printName)
Employee.printName()
