print("\n\n")
def apply_twice(func,arg,func2,arg2): #функция высшего порядка, принимает другую функцию в качестве аргумента
    return(func2(func(func(arg)+func2(arg2))))#каждая функция просто проделывает то,что в ней написано(прибавляет число)
def add_five(x):
    return x+5
def add_seven(u):
    return u+7
print(apply_twice(add_five,10,add_seven,500))
print("\n\n")

def pure_function(x,y):
    temp=x+2*y
    return temp/(2*x+y)
print(pure_function(50,20))
print("\n\n")
some_list=[]
def impure(arg):
    some_list.append(arg)
    print(some_list)
a=5
while a>0:
    arg=a
    a-=1
    impure(arg)
impure(some_list)
print("\n\n")

