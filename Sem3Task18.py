# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
 
arr=[]
sum = 0
j = 0
n = int(input("Введите кол-во элементов "))
for i in range(n):
    arr.append(random.randint(1,10))
X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - arr[0])
index = 0
for i in range(1, n):
    count = abs(X - arr[i])
    if count < min:
        min = count
        index = i
print(arr)
print(f'Число {arr[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - arr[index])}')