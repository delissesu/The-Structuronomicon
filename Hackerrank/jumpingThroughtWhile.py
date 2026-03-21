def printIncreasingPower(x):
    numCounter = 1
    while(numCounter**2 <= x):
        print (numCounter**2 , end = " ")
        numCounter += 1
        
def printIncreasingPower2(number: int) -> None:
    i : int = 1
    j : int = 1
    while (i <= number):
        if (i == (j**2)):
            print(i, end=' ')
            j += 1
            i += j
        else: i+=1

number = int(input())
printIncreasingPower2(number);print()
printIncreasingPower(number)