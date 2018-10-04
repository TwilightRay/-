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

#class Dog(Animal):
    #legs=4
    #def __init__(self,name,color):
     #   self.name=name
      #  self.color=color
    #def bark(self):
     #   print("Woof!")


class Wolf:
    legs = 4   #круто, этот параметр тоже наследуется
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
       print("Woof!")
husky = Dog("Max","grey")
husky.bark()

fido=Dog("Fido","brown")
print(fido.name)
fido.bark()
print(fido.legs)
print(Dog.legs)

class A:
    def method(self):
        print("A")
class B(A):
    def method1(self):
        print("B")
class C(B):
    def method2(self):
        print("C")
        super().method()#поиск метода по имени в суперклассе и вызывает его метод
c = C()
c.method()
c.method1()
c.method2()

B().method()

class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Vector2D(self.x+other.x, self.y+other.y)
first=Vector2D(5,7)
second=Vector2D(3,9)
result=first+second
print(result.x)
print(result.y)