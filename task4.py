#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число: '))
result = ''
while num > 0:
    y = str(num % 2)
    result = y + result
    num = int(num / 2)
 
print("Ваше число в двоичной системе счисления: ", result)