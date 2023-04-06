# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

A = int(input("Введите число "))
B = int(input("Введите степень "))

# print(pow(A, B))

def func(A, B):
    if B == 0:
        return 1

    return A * func(A, B - 1)


print(func(A, B))