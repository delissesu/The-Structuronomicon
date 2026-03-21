def removeDuplicates(arr):
    if not arr:
        return []
    
    result = []
    
    for num in arr:
        if num not in result:
            result.append(num)
            
    return result    

arr = [1, 2, 4]
print(removeDuplicates(arr))

def removeDuplicates1(arr):
    if not arr:
        return []
    
    temp = {}
    result = []
    
    for num in range(len(arr)):
        temp[arr[num]] = True
    
    for keys in temp:
        result.append(keys)
    
    result.sort()
    return result

print(removeDuplicates1(arr))

def removeDuplicates_twoPointer(arr):
    if not arr:
        return []
        
    i = 0  # slow pointer
    
    # j is fast pointer
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    
    
    """
    [2, 2, 2, 3, 5, 5]
    1. 2 == 2 -> skip
    2. 2 == 2-> skip
    3. 2 == 3? -> tidak, maka i akan geser satu dan arr[i] ganti ke value arr[j]
    
    4. list awal adalah [2, 2, 2, 3, 5, 5] diupdate menjadi [2, 3, 2, 3, 5, 5]
    5. cek lagi, arr[1] = 2 apakah sama dengan arr[4] = 5?
    6. Tidak, maka list diupdate menjadi [2, 3, 5, 3, 5, 5]
    7. cek lagi, apakah arr[2] == arr[5]?
    8. Karena loop terakhir, maka stop dan keluar dari perulangan
    
    9. I terakhir adalah 2, maka slice sebanyak i + 1
    10. [2, 3, 5, 3, 5, 5] -> slice i + 1 -> harus tambah satu agar semua elemen kereturn
    11. Jika hanya menggunakan i, maka eemen terakhir yang sudah diupdate maka tidak ikut
    
    
    """
    
    # Slice array to keep only unique elements
    return arr[:i + 1]

print(removeDuplicates_twoPointer(arr))