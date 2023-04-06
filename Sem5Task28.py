A = int(input("Введите первое число "))
B = int(input("Введите второе число "))

def sum(A, B):
    if B == 0:
        return A
    return 1 + sum(A, B - 1)

print(sum(A, B))