# Version 1
def leaderInArray(arr):
    counter = 0
    n = len(arr)
    result = []
    
    for i in range(0, n):
        if arr[i] >= counter:
            counter = arr[i]
            result.append(counter)
        else: i += 1
    
    return result[::-1]

arr = [16, 17, 4, 3, 5, 2]
print(leaderInArray(arr))

# Version 2
def leaderInArray2(arr):
    result = []
    n = len(arr)
    most_right = arr[-1]
    result.append(most_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] >= most_right:
            most_right = arr[i]
            result.append(most_right)
    
    return result[::-1]

print(leaderInArray2(arr))

# Version 3
def leaderInArray3(arr):
    n = len(arr)
    max_element = arr[-1]
    
    result = [max_element]

    for i in range(n - 2, -1, -1):
        if arr[i] < max_element:
            continue
        else:
            max_element = arr[i]
            result.append(max_element)
    
    return result[::-1]

print(leaderInArray3(arr))

# arr = [16, 17, 4, 3, 5, 2]
# suffix = [2] -> [-1] return -> 2
# suffix = [2, 5, 5, 5, 17, 17]
# reverse jadi [17, 17, 5, 5, 5, 2]

# cek lagi di arr setiap indeks i yang sama dengan di suffix

# Version 4
def leaderInArray4(arr):
    n = len(arr)
    suffix_list = [arr[n - 1]]  # Initialize with last element
    print("suffix",suffix_list)
    
    result = []
    
    for i in range(n - 2, -1, -1):
        # Find maximum between current element and previous suffix
        suffix_list.append(max(arr[i], suffix_list[-1]))
    
    suffix_list = suffix_list[::-1]  # Reverse the list
    
    print("suffix", suffix_list)
    
    for i in range(n):
        if arr[i] == suffix_list[i]:
            result.append(arr[i])
    
    return result

print(leaderInArray4(arr))

# Version 5
def leaderInArray5(arr):
    n = len(arr)
    result = []
    
    # arr = [16, 17, 4, 3, 5, 2]
    """
    i akan selalu gerak dari 0
    j mulainya dari 1
    
    """
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                break
        else:
            result.append(arr[i])
    
    return result

print(leaderInArray5(arr))        