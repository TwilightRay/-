print('\nПервый код:')
primary = {
    "red":[255,0,0],
    'green':[0,255,0],
    "blue":[0,0,255],
}
print(primary["red"])

print('\nВторой код:')

squares1 = {1:1,2:4,3:"error",4:16,}
print (squares1)
squares1[8]=64
squares1[3]=9
print (squares1)

print('\nТретий код:')

nums = {
    1:"one",
    2:"two",
    3:"three",
}
print(1 in nums)
print('three' in nums)
print(4 not in nums)

print('\nЧетвертый код:')

paris = {1:'apple',
         'orange':[2,3,4],
         True:False,
         None:'True'}
print(paris.get('orange')) #Поиск ключа
print(paris.get(7)) #По умолчанию NONE
print(paris.get(12345,'Not in dictonary')) #Если ключ не найден, возвращает указанное значение

print('\nПятый код (свой):')

test = {(5,6,7):"Test1",
        (9,90,70):"Test2"}
print((5,6,7)in test)
print(test.get((9,90,70)))

print('\nШестой код:')

words = ('spam','eggs','sausages',)
print (words[0])

my_tuple = "one", "two", "three"

print('\nСедьмой код:')

squares = [0,1,4,9,16,25,36,49,64,81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[7:])
print(squares[:3])
print(squares[::2])
print(squares[2:8:3])
print(squares[7:-1])
print(squares[::-1])


print('\nВосьмой код:')

cubes = [i**3 for i in range(5)]
print(cubes)
evens = [i**2 for i in range(10)if i**2%2==0]
print(evens)

print('\nДевятый код (свой):')

six = [i**2 for i in range(5*2)]
print(six)

print('\nДесяиый код (немного):')

nums1 = [4, 5, 6]
msg = "Numbers: {0}{1}{2}". format(nums1[0], nums1[2], nums1[1]) #получится вставить частицы списка в строчку
print(msg)
print("Numbers: {0}{1}{2}", nums1[0], nums1[2], nums1[1])#не получится вставить частицы списка в строчку
print("Numbers: {0}{1}{2}", 1, 2, 3) #это так не работает
print("Numbers: {0}{1}{2}".format( 1, 2, 3))#а работает вот так

print('\nОдиннадцатый код (немного):')

print(min(squares),max(squares),abs(-99),sum([5,4,8,55,654,45,4,55]))
a=min([sum([11,222]),max(abs(-30),2)])
print(a)

print('\nДвенадцатый код:')

num = [55,44,33,22,11]

if all([i>5 for i in num]): #хз зачем скобки, они необязательны
    print("Все числа больше 5")

if any(i%2==0 for i in num):#вот видишь
    print('Молодец')

for v in enumerate(num):
    print(v)

for k in squares:
    print (k)

