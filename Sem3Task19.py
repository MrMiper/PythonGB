#  Дана последовательность из N целых числе и число k. Необходимо сдвинуть всю последовательность на k элементов вправо.

arr = [1, 2, 3, 4, 5]
k = 3
for i in range(k):
    arr.insert(0, arr.pop(-1))
    print(arr)