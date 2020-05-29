import random

def sum(x):
    if len(x) == 1:
        return x[0]
    else:
        return sum(x[:len(x)//2]) + sum(x[len(x)//2:])

print(sum([1,3,4,5]))


def quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot_i = len(x) // 2
        pivot = x[pivot_i]
        less = []
        greater = []
        for i in range(len(x)):
            if i == pivot_i:
                continue
            e = x[i]
            if e < pivot:
                less.append(e)
            else:
                greater.append(e)
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([random.random() for _ in range(16)]))