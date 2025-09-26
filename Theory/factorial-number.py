number : int = int(input())
for i in range(number - 1, 0, -1):
    number *= i
print(number)