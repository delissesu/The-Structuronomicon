a, b, c = 1, 2, 4

# Version 1
def appendToList(a,b,c):
    result = []
    
    result.append(a)
    result.append(b)
    result.append(c)
    
    return result

print(appendToList(a,b,c))

# Version 2
def appenToList2(a,b,c):
    return [a, b, c]

print(appenToList2(a,b,c))

# Version 3
def appendToList3(a,b,c):
    return [num for num in (a, b, c)]

print(appendToList3(a,b,c))

#Version 4
def appendToList4(a,b,c):
    result = []
    
    result.extend([a, b, c])
    
    return result

print(appendToList4(a,b,c))