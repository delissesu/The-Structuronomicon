# Cara 1
number: list[int] = [int(num) for num in input().strip().split()]
print(number)
n: int = len(number)
results: list[int] = [number[0]]
print(results)
for i in range(1, n):
    results.append(number[i] + results[-1]) # Selalu jumlahkan dengan elemen terakhir di results
print(results)

# Cara 2
number: list[int] = [int(num) for num in input().strip().split()]
results: list[int] = []
running = 0
for val in number:
    running += val
    results.append(running)
print(results)
