def missingRanges(arr, lower, upper):
    ans = []
    prev = lower - 1
    for num in arr + [upper + 1]:  # sentinel to handle final gap
        if num - prev > 1:
            ans.append([prev + 1, num - 1])
        prev = num
    return ans

# arr = [-48, -10, -6, -4, 0, 4, 17]
arr = [14, 15, 20, 30, 31, 45]
# arr = [15, 16, 17, 18] 
lower = 10
upper = 50
# Output: [[10, 13], [16, 19], [21, 29], [32, 44], [46, 50]]
print(missingRanges(arr, lower, upper))

#Back-end complete function Template for Python 3
def missingRanges1(arr, lower, upper):
    res = []
    n = len(arr)

    # Check for missing range before the first element
    if lower < arr[0]:
        res.append([lower, arr[0] - 1])

    # Check for missing ranges between elements
    for i in range(n - 1):
        if arr[i + 1] - arr[i] > 1:
            res.append([arr[i] + 1, arr[i + 1] - 1])
            
    # for i in range(1, n - 1):
    #     if arr[i] - arr[i - 1] > 1:
    #         res.append([arr[i - 1] + 1, arr[i] - 1])

    # Check for missing range after the last element
    if upper > arr[-1]:
        res.append([arr[-1] + 1, upper])

    return res

print(missingRanges1(arr, lower, upper))

# Version 3
def missingRanges2(arr, lower, upper):
    ans = []
    n = len(arr)
    
    for i in range(n):
        if lower != arr[i]:
            ans.append([lower, arr[i] - 1])
        lower = arr[i] + 1

    if n > 0 and arr[-1] < upper:
        ans.append([arr[-1] + 1, upper])
    elif n == 0:  # Jika arr kosong, seluruh rentang adalah missing
        ans.append([lower, upper])
    
    # Hapus range yang tidak valid (misal [x, y] dengan x > y)
    ans = [rng for rng in ans if rng[0] <= rng[1]]
    return ans
            
print(missingRanges2(arr, lower, upper))

# Version 4
def myMissingRange3(arr, lower, upper):
    result = []
    n = len(arr)
    
    if lower < arr[0]:
        result.append([lower, arr[0] - 1])
        
    # arr = [14, 15, 20, 30, 31, 45]
    
    for i in range(1, n - 1):
        if arr[i + 1] - arr[i] > 1:
            result.append([arr[i] + 1, arr[i + 1] - 1])
            
    if upper > arr[-1]:
        result.append([arr[-1] + 1, upper])
    
    return result

print(myMissingRange3(arr, lower, upper))