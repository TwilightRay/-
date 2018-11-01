
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

print("\n\n")

num_set={1,2,3,4,5,1,5,7,8,6,1,5,6,8,7,2,3,6,9,8,5,2,1,4,7,8,5,2,3,6,1,4,5,6,9,8,7,3,1,}
print(num_set)
word_set = set(["world","privet","pochemu ti podcherkivaeshsya"])
print(3 in num_set)
print("spam" not in word_set)
print("\n\n")

num_set.add(-7)
print(num_set)
num_set.remove(2)#удаляет элемент, если его нет, то выдает ошибку
num_set.discard(555)#удаляет элемент, если он есть в кучке
while len(num_set)!=0:
    print(num_set)
    num_set.pop()
print("\n\n")

first={11,22,33,44,55,66,77,88,99,1,2,3,6,5,8,}
second={22,555,22,33,66,888,77,11,1,2,3,4,5,6,7,8,9,12,2,32,65,45,78,98}
print(first|second) #объединяет в одно, содержащее все эл-ты двух кучек
print(first&second) #возвращает только общие эл-ты
print(first-second) #только с первого
print(second-first) #только с первого
print(first^second) #симметричная разность-не возвращает общие эл-ты, а остальное выводит

print("\n\n")

a = {i * 2 for i in range(10)} # генератор множеств
print(a)

a = {i ** 2 for i in range(10)} # генератор множеств
while len(a)!=0:
    print(a)
    a.pop()
print("\n\n")
print(frozenset('qwerty'))
print("\n\n")


name = input('Vvedite vashe imya: ')
age = input('Vvedite, skolko vam let: ')
name='Vas zovut: '+name
age = 'Vam: '+age+' let.'
print(name)
print(age)

s = 'Elena Malisheva, Dmitry Nagiev, Andrey Malahov, Iosiv Kabzon, Garik Martirosyan'
x=input('Vvedite vashe imya: ')
if (x in s):
    print('Dobro pozhalovatt na prazdnik')
else:
    print('Izvinite. no vas net v spiske gostey')

sun = input('vvedite 1 esli pogoda solnechnaya i 2 esli pasmurnaya: ')
if(sun=='1'):
    d='nuzhno zagoratt'
else:
    d='zagoratt ne poluchitsya'
print(d)

myname=input('Введите логин: ')
mypass=input('Введите пароль: ')
if ((myname=='ivan')and(mypass=='superpassword123') or (myname=='marina')and(mypass=='marinka93')):

    print('Добро пожаловать, '+myname+"!")
else:
    print('До свидания.')


v=int(input('Введите ваш возраст: '))
if(v<18):
    print('Привет, йуный кодер')
elif(v<30):
    print('Здравствуйте, молодой человек')
elif(v<65):
    print("Добрый день. Как семья, как дети?")
elif(v<100):
    print('Здорова, Михалыч, пенсию уже выдали?')
elif(v>100):
    print('Клан бессмертных приветствует тебя!')

if sun==True and season=='Лето':
    emotion="Ура, лето!"
    print(emotion)

x = int(input('Введите число '))
if not x>10:
    print('Все верно, число не больше десяти')
else:
    print('К сожалению, ваше число больше десяти.')

if (car==1 or money>1000) and beauty==1:
    print('Девушка с дискотеки будт ваша.')
else:
    print('Вам ничего не светит.')



a=[67,5,90,20,30]
b=['Маша','Ваня','Лена','Марина','Арнольд']
print(a[2])
print(a[0])
print(b[1])
b=['Вика']
b.append('Андрей')
print(b[-1])
a.sort()