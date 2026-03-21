# Sample Output -> 5 10 15 20 25 30 35 40 45 50

def multiplicationTable(N : int):
    for i in range(1, 11):
        print(N * i, end=" ")
        
multiplicationTable(5)