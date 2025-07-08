number: list[int] = [int(num) for num in input().strip().split()]
results: list[int] = [len(number)]
for i in range(1, len(number)):
    results[i] = number[i] + results[i - 1]
print(results)