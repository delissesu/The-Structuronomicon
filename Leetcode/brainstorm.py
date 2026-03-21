num = 121
num = str(num)

listNumber = []

for character in num:
    print(character)
    listNumber.append(character)
    
print(listNumber)

numl = ['1', '2', '1'] # Sama dengan list(str(121))
var1 = numl[::-1]
print(numl == var1)