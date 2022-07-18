#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
#максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import randint
n = int(input('Введите количество элементов массива: '))
arr = []
newarr=[]
for i in range(n):
    n = randint(100, 10000) / 100
    arr.append(n)
print(arr)

for i in range(len(arr)):
    a = arr[i] - int(arr[i])
    newarr.append(round(a, 2))
result = round(max(newarr) - min(newarr), 2)
print('Разница между максимальным и минимальным значением дробной части: ', result)

