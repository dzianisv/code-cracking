
def find_max(arr):
    if len(arr) == 0:
        return None
    
    max = arr[0]
    for i in arr[1:]:
        if i > max:
            max = i
        else:
            break
    return max


def find_max2(arr):
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    
    s = len(arr) 
    v = arr[s//2]
    l_i = s//2-1 
    l = arr[l_i] 
    
    
    if v > l:
        return find_max2(arr[l_i+1:])
    elif v < l:
        # did mistake here, python slices doesn't include second index: [i:j)
        # return fin_max2(arr[:l_i])
        return find_max2(arr[:l_i+1])

print(find_max2([1, 5, 3, 2]))
print(find_max2([1, 2, 5, 8]))
print(find_max2([3, 4, 5, 3, 4, 8, 0]))
print(find_max2([1, 2, 5, 8, 4, 1, 0]))
print(find_max2([1, 5]))
print(find_max2([1, 5, 3]))
print(find_max2([5]))

