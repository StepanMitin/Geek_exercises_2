#1. Создать список и заполнить его элементами различных типов данных. 
# Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. 
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['Peter', 'Vlad', 50, True, 567.3 ,[list]]

print(my_list)

print(my_list[0], '\n', my_list[1], '\n', my_list[2], '\n',my_list[3], '\n', my_list[4], '\n', my_list[5] )
print(type(my_list[0]), '\n', type(my_list[1]), '\n', type(my_list[2]), '\n',type(my_list[3]), '\n', type(my_list[4]), '\n', type(my_list[5]))

#2. Для списка реализовать обмен значений соседних элементов, т.е. 
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. 
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = ['Peter', 'Vlad', 50, True, 567.3 ,[list]]

a = input("Enter your phrase or number: ")
b = input("Enter your phrase or number: ")

my_list.append(a)
my_list[3] = b

print(my_list)
my_list[0]= my_list[1]
my_list[1]= my_list[2]
my_list[2]= my_list[3]
my_list[3]= my_list[4]
my_list[4]= my_list[5]
my_list[5]= my_list[0]
print(my_list)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#  Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
# Напишите решения через list и через dict.

my_list = {'1' : 'january', '2' : 'february', '3' : ' march', '4' : 'april', '5' : 'may', '6' : 'june', '7' : 'jule', '8' : 'august', '9' : 'septemebr', '10' : 'october', '11' : 'nevember', '12' : 'december'}
number = input('Enter number a month: ')


print(my_list[number])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

string = input('Enter your words: ')

words = string.split()
for num, word in enumerate(words):
    print(num, word[:10])

# 5. 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
# У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, 
# то новый элемент с тем же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].    

rating = [7, 5, 3, 3, 2]
element = int(input(' Enter new number rating: '))
rating.append(element)
print(sorted(rating))

# 6. * Реализовать структуру данных «Товары». 
# Она должна представлять собой список кортежей. 
# Каждый кортеж хранит информацию об отдельном товаре. 
# В кортеже должно быть два элемента — номер товара и словарь с параметрами -
# (характеристиками товара: название, цена, количество, единица измерения). 
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

product1 = {'product_name': 'computer ', 'price': 500, 'volume': 5, 'sum': 2500}
product2 = {'product_name': 'scaner', 'price': 300, 'volume': 3, 'sum': 900}
product3 = {'product_name': 'printer', 'price': 200, 'volume': 3, 'sum': 600}

user1 =  input('Enter product name: product1 or product2 or product3 ')
if user1 == 'product1':
    print(product1['product_name'])
    print(product1['price'])
    print(product1['volume'])
    print(product1['sum'])
elif user1 == 'product2':
    print(product2['product_name'])
    print(product2['price'])
    print(product2['volume'])
    print(product2['sum'])
elif user1 == 'product3':
    print(product3['product_name'])
    print(product3['price'])
    print(product3['volume'])
    print(product3['sum'])
else:
    print('you do not slect posititon')     