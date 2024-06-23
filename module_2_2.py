# Задача "Все ли равны?":


print('Проверка на равенство введенных числел')
print('Введите число №1: ')
first = int(input())
print('Введите число №2: ')
second = int(input())
print('Введите число №3: ')
third = int(input())
if first == second and second == third:
    print('Все три числа равны')
    print(3)
elif first == second or second == third or first == third:
    print('Между введенными числами есть два одинаковых')
    print(2)
else:
    print('между введенными числами одинаковых нет')
    print(0)