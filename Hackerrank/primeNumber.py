number : int = int(input())

if number in [0, 1]:
    print("Not a prime number")
elif number == 2:
    print("Prime number")
else:
    primeNumber : bool = True
    
    for i in range(2, number):
        if number % i == 0:
            primeNumber = False
            break
    
    if primeNumber:
        print("Prime number")
    else:
        print("Not a prime number")