# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите количество элементов чисел Фибоначчи: '))
fib_pos = [0,1,1]
fib_neg = [-1, 1]
def Fib(n):
    f1 = 1
    f2 = -1
    i = 2
    while (i < n): 
        i += 1
        s = f1 - f2
        f1 = f2
        f2 = s
        fib_neg.insert(0,s) 
Fib(n)

def Fib(n):
    f1 = f2 = 1
    i = 3
    while (i < n+1): 
        i += 1
        s = f1 + f2
        f1 = f2
        f2 = s
        fib_pos.append(s) 
Fib(n)
print(fib_neg+fib_pos)