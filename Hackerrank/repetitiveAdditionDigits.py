# Version 1
def singleDigit(n):
    if n == 0:
        return 0
    
    while n > 9:
        sum = 0
        
        while n:
            sum += n % 10
            n //= 10
        
        n = sum
    
    return n

number = int(input())
print(singleDigit(number))

# Version 2
def singleDigit2(n):
    if n == 0:
        return 0
    
    if n % 9 == 0:
        return 9
    else:
        return n % 9
    
print(singleDigit2(number))