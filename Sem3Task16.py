#  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
 
arr=[]
sum = 0
j = 0
n = int(input("Введите кол-во элементов "))
for i in range(n):
    arr.append(random.randint(1,10))
num = int(input("Введите число, которое хотите найти (от 1 до 10) "))
while j < len(arr):
    if arr[j] == num:
        sum = sum + 1
    j = j + 1
print([arr])
print(f"Число {num} встречается {sum} раз")