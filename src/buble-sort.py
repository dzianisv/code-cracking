import random

arr = [random.random() for _ in range(128)]

def buble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)-i-1):
            print(i, j)
            if (arr[i] > arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(arr)
print(buble_sort(arr))