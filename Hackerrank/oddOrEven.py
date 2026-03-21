num : int = int(input())

if num % 2 == 0:
    print("Evem")
else:
    print("Odd")    
    
# Use Lambda
numList : list[int] = list(map(int, input().split()))
evenNumbers : list[int] = list(filter(lambda num : (num % 2 == 0), numList))
oddNumbers : list[int] = list(filter(lambda num : (num % 2 != 0), numList))
print(evenNumbers);print(oddNumbers)

def CheckNumOddorEven(numbers : list[int]) -> tuple[list[int], list[int]]:
    evenNumbers : list[int] = list(filter(lambda x : (x % 2 == 0), numbers))
    oddNumbers : list[int] = list(filter(lambda x : (x % 2 != 0), numbers))
    return evenNumbers, oddNumbers

print(CheckNumOddorEven(numList))