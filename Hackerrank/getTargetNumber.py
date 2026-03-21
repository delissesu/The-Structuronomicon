list_number : list[int] = list(map(int, input().split()))
target_number : int = int(input())

def searchNumBasic(num : list[int], target : int) -> int:
    for i, number in enumerate(num):
        if number == target:
            return i
    
    return -1

print(searchNumBasic(list_number, target_number))

def searchNaive(num, target):
    for i in range(len(num)):
        if num[i] == target:
            return i
    
    return -1

print(searchNaive(list_number, target_number))