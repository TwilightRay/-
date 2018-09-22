print("\n\n")
def apply_twice(func,arg,func2,arg2): #функция высшего порядка, принимает другую функцию в качестве аргумента
    return(func2(func(func(arg)+func2(arg2))))#каждая функция просто проделывает то,что в ней написано(прибавляет число)
def add_five(x):
    return x+5
def add_seven(u):
    return u+7
print(apply_twice(add_five,10,add_seven,500))