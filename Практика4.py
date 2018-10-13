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

class Def:
    def __init__(self, cont):
        self.cont = cont

class SpecialString(Def):
    def __truediv__(self, other):
        line="="*len(other.cont)
        return "\n".join([self.cont,line,other.cont])

spam=SpecialString("spam")
hello=SpecialString("Hello world")
print(spam/hello)

class SpecialString1(Def):
    def __gt__(self,other):
        for index in range(len(other.cont)+1):
            result=other.cont[:index]+">"+self.cont
            result+=">"+other.cont[:index]
            print(result)

spam = SpecialString1("spam")
eggs = SpecialString1("eggs")
spam > eggs

import random
class VagueList(Def):
    def __getitem__(self, index):
        return self.cont[index+random.randint(-1,1)]

    def __len__(self):
        return random.randint(0,len(self.cont)*2)

vague_list=VagueList(["A","B","C","D","E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    def push (self,value):
        self._hiddenlist.insert(0,value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

class Spam:
    __egg=7
    def print_egg(self):
        print(self.__egg)
s=Spam()
s.print_egg()
print(s._Spam__egg)
#print(s.__egg) ошибка не существует егга

class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height
    def calculate_area(self):
        return self.width*self.height
    @classmethod
    def new_square(cls, side_lenght):
        return cls(side_lenght, side_lenght)
square=Rectangle.new_square(5)
print(square.calculate_area())

class Pizza:
    def __init__(self, toppings):
        self.toppings=toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rd1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Integer!")

pizza = Pizza(["cheese","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed=True
print(pizza.pineapple_allowed)