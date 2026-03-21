def findUnion(a, b):
    union_list = []
    # Add unique elements from first array
    for num in a:
        if num not in union_list:
            union_list.append(num)
    
    # Add unique elements from second array
    for num in b:
        if num not in union_list:
            union_list.append(num)
    
    # Sort the result
    union_list.sort()
    return union_list

a = [1, 2, 1, 1, 2]
b = [2, 2, 1, 2, 1]

print(findUnion(a, b))


# Version 2
def FindUnion2(list1, list2):
    track = set()
    union_number = []
    
    for arr in [list1, list2]:
        for number in arr:
            if number not in track:
                track.add(number)
                union_number.append(number)
                
    return union_number

print(FindUnion2(a, b))

# Version 3
def FindUnion3(list1, list2):
    num_track = {}
    
    for num in range(len(list1)):
        num_track[list1[num]] = 1
    
    for num in range(len(list2)):
        num_track[list2[num]] = 1
        
    result = []
    
    for num_keys in num_track:
        result.append(num_keys)
    
    result.sort()
    return result

print(FindUnion3(a, b))