# # Naive Solution
# def sumTwoNum(num: list[int], target: int) -> list[int]:
#     len_num = len(num)

#     for i in range(len_num):
#         for j in range(i + 1, len_num):
#             sum = num[i] + num[j]

#             if sum == target:
#                 return [i + 1, j + 1]

#     return []


# num_list: list[int] = list(map(int, input().split()))
# target: int = int(input())

# result = sumTwoNum(num_list, target)
# print(result)


# # Two Pointer
# def sumTwoNumPointer(num: list[int], targetNumber: int) -> list[int]:
#     right_pointer: int = len(num) - 1
#     left_pointer: int = 0

#     while left_pointer < right_pointer:
#         sum = num[left_pointer] + num[right_pointer]

#         if sum == targetNumber:
#             return [left_pointer + 1, right_pointer + 1]
#         elif sum < targetNumber:
#             left_pointer += 1
#         else:
#             right_pointer -= 1

#     return []


# result = sumTwoNumPointer(num_list, target)
# print(result)


def naiveSolution(list_number, target):
    for i in range(len(list_number)):
        for j in range(i + 1, len(list_number)):
            if list_number[i] + list_number[j] == target:
                return [i + 1, j + 1]


listNumber = [7, 2, 11, 15]
targetNumber = 9
print(naiveSolution(listNumber, targetNumber))


def twoSumPointer(listNumber, target):
    left = 0
    right = len(listNumber) - 1

    while left < right:
        sumNumber = listNumber[left] + listNumber[right]
        if sumNumber == target:
            return [left + 1, right + 1]
        elif sumNumber < target:
            left += 1
        else:
            right -= 1

    return []


print(twoSumPointer(listNumber, targetNumber))
