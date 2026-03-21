# Pattern 1
for i in range(5):
    for j in range(5 - i - 1):
        print(end=" ")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
    
num : int = int(input())

# Pattern 2
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end='')
    
    for j in range(1, 2*i):
        print("*", end='')

    print()

# Pattern 3
for i in range(num):
    for j in range(num - i - 1):
        print(end=' ')
        
    for j in range(2 * i + 1):
        print("*", end='')
    
    print()

print()

# Pattern 4
for i in range(num, 0, -1):
    for j in range(num - i):
        print(end=' ')
        
    for j in range(2 * i - 1):
        print("*", end='')
    
    print()

# Pattern 4
print("INI PATTERN 4")
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print()
    
# Patterm 5
print("ini pattern 5")
for i in range(1, num + 1):
    random_number : int = 1 
    for j in range(1, i + 1):
        print(random_number, end='')
        
        random_number += 1
    
    print()

# Pattern 6
print("Pattern 6")
ascii_number : int = 65
for i in range(1, num + 1):
    for j in range(1, i + 1):
        print(chr(ascii_number), end=' ')
    
    ascii_number += 1
    print()
    
# Pattern 7
print("pattern 7")
for i in range(num, 0, -1):
    for j in range(1, i + 1):
        print("*", end=' ')
        
    print()

# Pattern 8 : same result w pattern 7
for i in range(num, 0, -1):
    for j in range(i):
        print("*", end=' ')
    
    print()
    
# Pattern 9
for i in range(num, 0, -1):
    for j in range(num - i):
        print(" ", end='')
    
    for j in range(i):
        if j == 0 or j == i - 1 or i == num:
            print("*", end='')
        else:
            print(" ", end='')
    
    print()
    
# Pattern 10
alph = 65
for i in range(1, num + 1):
    for j in range(num - i):
        # print(end=' ')
        print(" ", end='')
        
    for j in range(1, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()
    
# Pattern 11
for i in range(1, num + 1):
    for j in range(num - i):
        print(" ", end='')
        
    for k in range(2 * i - 1):
        print(k + 1, end='')
    
    print()
    
# Pattern 12
for i in range(num, 0, -1):
    for j in range(num - i):
        print(" ", end='')
        
    for k in range(2 * i - 1):
        print(k + 1, end='')
    
    print()
    
# Pattern 13
for i in range(1, num + 1):
    for j in range(1, 2*num):
        if j == num - i + 1 or j == num + i - 1 or i == num:
            print("*", end='')
        else:
            print(" ", end='')
    
    print()