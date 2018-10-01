class Student:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print("Hi from "+ self.name)
s1=Student("Amy")
s1.sayHi()
test=Student("Bob")

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
rect=Rectangle(7,8)
print(rect)


class Animal:  #суперкласс
    def __init__(self,name,color):
        self.name=name
        self.color=color

class Cat(Animal): #наследуемый класс
    #def __init__(self,color,legs): а низя
    #   self.color=color
    #  self.legs=legs
    def purr(self):
        print("Purr...")

#felix=Cat("Ginger",4)
#print(felix.color)
#rover=Cat("dog-colored",4)
#stumpy=Cat("brown",3)

class Dog(Animal):
    legs=4
    #def __init__(self,name,color):
     #   self.name=name
      #  self.color=color
    def bark(self):
        print("Woof!")
fido=Dog("Fido","brown")
print(fido.name)
fido.bark()
print(fido.legs)
print(Dog.legs)


