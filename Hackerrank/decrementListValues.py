arr = [324, 5, 2, 2]

# Version 1
def decrementList(arr):
    for number in range(0, len(arr)):
        arr[number] -= 1
        
    return arr

print(decrementList(arr))

# Version 2
def decrementList2(arr):
    p = [x - 1 for x in arr]
    return p

print(decrementList2(arr))

# Version 3
def decrementList3(arr):
    res = list(map(lambda x : x - 1, arr))
    
    return res

print(decrementList3(arr))

# Version 3
def decrementList4(arr):    
    return list(map(lambda x : x - 1, arr))

print(decrementList4(arr))