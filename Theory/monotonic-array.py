ex_array = [8, 7, 4, 3, 21, 1]

# for i in range(len(ex_array) - 1):
#     p = ex_array[i + 1]
#     p2 = ex_array[i]
    
#     if (p >= p2) or (p <= p2) : 
#         print("True")
#     else:
#         print("Else")
    
def monotonicArray(arr):
    if len(arr) <= 1:
        return True

    non_decrease = True
    non_increase = True

    for i in range(len(arr) - 1):
        print("inii value increase", non_increase, i)
        print("inii value decrease",non_decrease, i)
        if arr[i] > arr[i + 1]:
            non_decrease = False
        if arr[i] < arr[i + 1]:
            non_increase = False
        if not non_decrease and not non_increase:
            print(arr[i], arr[i + 1])
            return False
    
    return True

print(monotonicArray(ex_array))