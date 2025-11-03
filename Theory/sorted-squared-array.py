random_array = list(map(int, input().split()))
# sorted_array = [x ** 2 for x in sorted_array]
# print(sorted_array)

def sortSquared(arrayInput):
    return [x ** 2 for x in arrayInput]

sortSquare = sortSquared(random_array)

def sortIncrease(squaredArr):
    for _ in range(len(squaredArr)):
        for j in range(len(squaredArr) - 1):
            if squaredArr[j] > squaredArr[j + 1]:
                squaredArr[j + 1], squaredArr[j] = squaredArr[j], squaredArr[j + 1]
    
    return squaredArr

print(*sortIncrease(sortSquare))