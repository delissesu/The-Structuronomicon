number : int = int(input())

for i in range(1, number + 1):
    listNumber = []
    
    for j in range(1, (i + 1)):
        print(j, sep=' ', end=' ')
        
        if (j < i):
            print("+", sep=" ", end=" ")
        
        listNumber.append(j)
    
    print("=", sum(listNumber))