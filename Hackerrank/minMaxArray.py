# # Version 1
# def get_min_max(arr):
#         minimum = min(arr)
#         maximum = max(arr)
#         return minimum, maximum

# # Test case
# array = [3, 2, 1, 56, 10000, 167]
# print(get_min_max(array))

# # Version 2
# def GetMinMax(list):
#     minimum = list[2]
#     maximum = list[2]
    
#     for number in list:
#         if number < minimum:
#             minimum = number
        
#         if number > maximum:
#             maximum = number
    
#     return minimum, maximum

# print(GetMinMax(array))

# # Version 3
# def GetMinMax2(list):
#     minimum = list[0]
#     maximum = list[0]
    
#     for i in range(1, len(list)):
#         if list[i] < minimum:
#             minimum = list[i]
        
#         if list[i] > maximum:
#             maximum = list[i]
    
#     return minimum, maximum

# print(GetMinMax2(array))

# def GetMinMax3(list):
#     if not list:
#         return None, None
    
#     if len(list) == 1:
#         return list[0], list[0]
    
#     if len(list) == 2:
#         if list[0] < list[1]:
#             return list[0], list[1]
#         else:
#             return list[1], list[0]
    
#     minimum = list[0]
#     maximum = list[0]
    
#     for number in list[1:]:
#         if number < minimum:
#             minimum = number
        
#         if number > maximum:
#             maximum = number
        
#     return minimum, maximum

# print(GetMinMax3(array))

# # Tes
# def minMax(listNumber):
#     if not listNumber:
#         return None, None
    
#     n = len(listNumber)
    
#     if n == 1:
#         return listNumber[0], listNumber[0]
#     elif n == 2:
#         if listNumber[0] < listNumber[1]:
#             return listNumber[0], listNumber[1]
#         else:
#             return listNumber[1], listNumber[0]
        
#     minimum = listNumber[0]
#     maximum = listNumber[0]
    
#     for number in listNumber[1:]:
#         if number < minimum:
#             minimum = number
        
#         if number > maximum:
#             maximum = number
    
#     return minimum, maximum

# listNumber = [1, 2, 3, 31, 21]
# print(minMax(listNumber))

def inputToList(a, b, c):
    newList = []
    
    for number in a, b, c:
        newList.append(number)
        
    return newList
        
a, b, c = map(int, input().split())
print(inputToList(a, b, c))