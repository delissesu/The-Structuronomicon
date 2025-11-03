random_array = list(map(int, input().split()))
# sorted_array = [x ** 2 for x in sorted_array]
# print(sorted_array)

def sortSquared(arrayInput):
    return [x ** 2 for x in arrayInput]

sortSquare = sortSquared(random_array)

for i in range(len(sortSquare)):
    for j in range(len(sortSquare) - 1):
        if sortSquare[j] > sortSquare[j + 1]:
            sortSquare[j + 1], sortSquare[j] = sortSquare[j], sortSquare[j + 1]

print(*sortSquare)