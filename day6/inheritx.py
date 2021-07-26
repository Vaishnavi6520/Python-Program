class Cars:
    def myColor(self,color):
        self.color=color
        print(self.color)

class BMW(Cars):
    def topSpeed(self,speed):
        self.speed=speed
        print(self.speed)

objcars=Cars()
objBMW=BMW()
# objcars.myColor("Red")
# objcars.topSpeed(100)
objBMW.myColor("white")
objBMW.topSpeed(150)

        