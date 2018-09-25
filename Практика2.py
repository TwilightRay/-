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

def my_func(f,arg):
    return f(arg)
print(my_func(lambda x: 2*x*x, 5))
print("\n\n")
def polynomial(x):
    return x**2+x+4
print(polynomial(-4))
print("\n\n")
print((lambda x: x**2+5*x+4)(10))
print("\n\n")
double=lambda x: x*2
print(double(7))
print("\n\n")
triple=lambda x: x*3
add=lambda x, y: x+y
print(add(triple(3),4))
print("\n\n")

#add_five
nums=[11,22,33,44,55]
result=list(map(add_five,nums))
print(result)

result1=list(map(lambda x:x+5,nums))
print(result1)

print("\n\n")

res=list(filter(lambda x:x%2==0,nums))
print(res)

print("\n\n")

def countdown():
    i=5
    while i>0:
        yield i
        i -= 1
for i in countdown():
    print(i)