# @param x: int
# @return: bool

def checkOddEven(x : int) -> int:
    # code here
    if x % 2 == 0:
        return True
    else:
        return False
        
number : int = int(input())
print(checkOddEven(number))