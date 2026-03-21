def rearrange(arr):
    negative_num = []
    positive_num = []
    
    for number in arr:
        if number < 0:
            negative_num.append(number)
        else:
            positive_num.append(number)
            
    result = []

    min_length = min(len(positive_num), len(negative_num))
    
    # positive di index genap, negative di ganjil
    for i in range(min_length):
        # print(positive_num[i], negative_num[i])
        # print(positive_num, negative_num)
        result.append(positive_num[i]) 
        result.append(negative_num[i]) 

    
    # Tambahkan sisa elemen yang belum diproses
    # Start dengan indeks min_length karena perulangan terakhir tidak include
    if len(positive_num) > min_length:
        result.extend(positive_num[min_length:])
    elif len(negative_num) > min_length:
        result.extend(negative_num[min_length:])
    
    return result

arr = [9,-1, 31, 2, -3, 21]
print(rearrange(arr))


# class Solution:

#     def rearrange(self, arr):
#         # Initialize two lists to store positive and negative numbers
#         pos = []
#         neg = []
#         n = len(arr)
#         # Iterate through the input array and separate positive and negative numbers
#         for i in range(n):
#             if arr[i] < 0:
#                 neg.append(arr[i])
#             else:
#                 pos.append(arr[i])

#         # Initialize variables for iteration through pos and neg lists
#         i = 0
#         j = 0
#         k = 0

#         # Merge the positive and negative numbers alternatively into the result array
#         while i < len(neg) and j < len(pos):
#             arr[k] = pos[j]
#             j += 1
#             k += 1
#             arr[k] = neg[i]
#             i += 1
#             k += 1

#         # If there are remaining positive or negative numbers, add them to the result array
#         while j < len(pos):
#             arr[k] = pos[j]
#             j += 1
#             k += 1

#         while i < len(neg):
#             arr[k] = neg[i]
#             i += 1
#             k += 1


# """ 
# Initialize two lists to store positive and negative numbers
# Iterate through the input array and separate positive and negative numbers
# Merge the positive and negative numbers alternatively into the result array
# If there are remaining positive or negative numbers, add them to the result array 
# """

def rearrange1(arr):
    # Pisahkan elemen positif dan negatif
    positive = []
    negative = []
    
    for num in arr:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    
    # Bersihkan array asli
    arr.clear()
    
    """
    pos 3, neg 4
    
    i = 0 -> last acces indexnya misal ke pos, mentok cuman di 2 -> 0, 1, 2
    tapi tetap diupdate ke angka 3
        
    """
    
    # Alternating elemen positif dan negatif
    i = 0
    while i < len(positive) and i < len(negative):
        arr.append(positive[i])
        arr.append(negative[i])
        i += 1
    
    # Tambahkan elemen positif yang tersisa
    while i < len(positive):
        arr.append(positive[i])
        i += 1
    
    # Tambahkan elemen negatif yang tersisa
    while i < len(negative):
        arr.append(negative[i])
        i += 1
    
    return arr

print(rearrange1(arr))