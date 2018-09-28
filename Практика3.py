class Cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
felix=Cat("Ginger",4)
print(felix.color)
rover=Cat("dog-colored",4)
stumpy=Cat("brown",3)

class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print("Woof!")
fido=Dog("Fido","brown")
print(fido.name)
fido.bark()