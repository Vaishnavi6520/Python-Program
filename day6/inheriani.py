class Animal:  
    def speak(self):  
        print("Animal Speaking")    
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
class Puppy(Animal):  
    def eating(self):  
        print("dog eating") 
d = Dog()
d = Puppy()
d.bark()  
d.speak() 
d.eating() 