#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
n = int(input('Введите количество элементов массива: '))
arr = []
mult = 0
for i in range(n):
   arr.append(random.randint(1,10))
print(arr)


newList=[]
if n%2==0:
    for i in range(0,len(arr)//2):
        sum = arr[i]*arr[-1-i]
        newList.append(sum)
    print(newList)
else: print("Введите четное количество элементов массива и попробуйте снова")