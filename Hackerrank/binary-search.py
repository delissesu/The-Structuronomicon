# Iterative Version
def binSearch(num: list[int], target: int) -> int:
    left: int = 0
    right: int = len(num) - 1

    while left <= right:
        middle: int = (left + right) // 2

        if num[middle] == target:
            return middle
        elif num[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


number: list[int] = list(map(int, input().strip().split()))
print(binSearch(number, 9))

# Recursive Version
def binarySearch(listNumber: list[int], left: int, right: int, targetNum: int) -> int:
    if left <= right:
        mid: int = (left + right) // 2

        if listNumber[mid] == targetNum:
            return mid
        elif targetNum > listNumber[mid]:
            return binarySearch(listNumber, mid + 1, right, targetNum)
        else:
            return binarySearch(listNumber, left, mid - 1, targetNum)

    return -1


numberList: list[int] = list(map(int, input().strip().split()))
print(binarySearch(numberList, 0, len(numberList) - 1, 9))


# Ascen and Descend Version
def findBinaryMix(listNumber: list[int]) -> int:
    ml: int = 0
    mr: int = len(listNumber) - 1

    while ml < mr:
        med: int = (ml + mr) // 2

        # Bandingin antara index mid sekarang dengan sebelahnya
        if listNumber[med] < listNumber[med + 1]:
            ml = med + 1

        if listNumber[med] > listNumber[med + 1]:
            mr = med

    # Mau kiri atau kanan terserah
    return ml


listTest: list[int] = [10, 20, 100, 80, 50]
print(findBinaryMix(listTest))
