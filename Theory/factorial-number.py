# number : int = int(input())
# for i in range(number - 1, 0, -1):
#     number *= i
# print(number)

str_nama = 'AdItyA DwI OmAgAAAt'
vokal = ['a', 'i', 'u', 'e', 'o']
jumlah = len([char for char in str_nama.lower() if char in vokal])
print(jumlah)

# faktoria
num = 5
for i in range(num-1, 0, -1): num *= i
print(num)

# fib
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n- 2)
print(fib(5))

# prime
def prime(num):
    if num <= 1:
        return False
    
    for i in range(2, num):
        if num % i == 0: 
            return False
    else:
        return True

print(prime(5))