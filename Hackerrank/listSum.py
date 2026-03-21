# Input: arr = [54, 43, 2, 1, 5]
# Output: 105
# Explanation: Just sum it 54 + 43 + 2 + 1 + 5 = 105.

arr = [54, 43, 2, 1, 5]

# Version 1
def listSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

# Version 2
def listSum2(arr):
    first_element = arr[0]
    last_element = arr[-1]
    
    sum = first_element + last_element
    
    for i in range(1, len(arr) - 1):
        sum += arr[i]
    
    return sum

print(listSum(arr))
print(listSum2(arr))

# Version 3
def listSum3(arr):
    sum = 0
    i = 0
    
    while i < len(arr):
        sum += arr[i]
        i += 1
    
    return sum

print(listSum3(arr))

# Version 4
def listSum4(arr):
    return sum(arr)

print(listSum4(arr))

    