symValue = {
    'I' : 1,
    'V' : 5, 
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

s : list[str] = list(map(str, input().upper()));print(*s)

# for k, v in symValue:
#     print(symValue[k], symValue[v])
    # for i in range(0, len(s)):

# symValueList = list(symValue.values());print(symValueList)
symValueList = [*symValue.values()]
print(symValueList)
print([*symValue.keys()])
print([v for v in symValue.values()])

n = {
    1 : 3,
    3 : 6,
    9 : 10
}

print([v for v in n.keys()])

total : int = 0


"""
SXVII
S NO
X YES
V YES
I YES
I YES
"""

notListed : list[str] = []
listed : list[str] = []

# counter : int = 0

# for key, value in symValue.items():
#     for char in s:
#         counter += 1
#         print("Ini char:" , char)
#         if (char == key): listed.append(char)
#         else: notListed.append(char)
            
            
# print(counter)
# print(notListed)
# print(listed)

for char in s:
    if char in symValue: listed.append(char)
    else: notListed.append(char)
    
print(listed, notListed)