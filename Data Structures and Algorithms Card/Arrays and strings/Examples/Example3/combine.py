import random

def combine(arr1, arr2):
    i, j, k = 0, 0, 0
    n = len(arr1)
    m = len(arr2)
    result = [0] * (n + m)
    
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
            k += 1
        else:
            result[k] = arr2[j]
            j += 1
            k += 1

    while i < n:
        result[k] = arr1[i]
        i += 1
        k += 1

    while j < m:
        result[k] = arr2[j]
        j += 1
        k += 1

    return result



lyst1 = [random.randint(1, 100) for i in range(10)]
lyst2 = [random.randint(1, 100) for i in range(10)]
lyst1.sort()
lyst2.sort()
print(lyst1)
print(lyst2)
print(combine(lyst1, lyst2))
