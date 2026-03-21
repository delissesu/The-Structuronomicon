arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 6, 7, 8]

def intersectionArr(arr1, arr2):
    result = []
    pointer_one = 0
    pointer_two = 0
    
    while pointer_one < len(arr1) and pointer_two < len(arr2):
        if arr1[pointer_one] == arr2[pointer_two]:
            if not result or result[-1] != arr1[pointer_one]:
                result.append(arr1[pointer_one])
            
            pointer_one += 1
            pointer_one += 1
            
        elif arr1[pointer_one] < arr2[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1
    
    return result

print(intersectionArr(arr1, arr2))

# Version 2
def intersectionArr2(arr1, arr2):
    arr1.sort()
    arr2.sort()
    
    result = []
    pointer_one = 0
    pointer_two = 0
    
    while pointer_one < len(arr1) and pointer_two < len(arr2):
        if arr1[pointer_one] == arr2[pointer_two]:
            if not result or result[-1] != arr1[pointer_one]:
                result.append(arr1[pointer_one])
            
            pointer_one += 1
            pointer_one += 1
            
        elif arr1[pointer_one] < arr2[pointer_two]:
            pointer_one += 1
        else:
            pointer_two += 1
    
    return result

print(intersectionArr2(arr1, arr2))

# Version 3
def intersectionArr3(arr1, arr2):
    result = []
    
    for num1 in arr1:
        if num1 in arr2 and num1 not in result:
            result.append(num1)
    
    return result

print(intersectionArr3(arr1, arr2))

# Version 4
def interesctionArr4(arr1, arr2):
    dict_track = {}
    result = []
    
    for num1 in arr1:
        dict_track[num1] = True
        
    for num2 in arr2:
        if num2 in dict_track and num2 not in result:
            result.append(num2)
    
    return result

print(interesctionArr4(arr1, arr2))