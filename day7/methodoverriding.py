class Car:
    def color(self):
        print("Blue")

class BMW(Car):
    def color(self):
        print("Black")

obj=BMW()
obj.color()

obj=Car()
obj.color()