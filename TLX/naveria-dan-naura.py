x = input()
if x[-1] == ".": x = x[:-1]

y = x.split(' ')

z = ""
a = 0

for i in range(len(y)):
    b = y[i]

    c = 0
    d = 0
    
    for j in range(len(b)):
        if b[j].islower():
            c += 1
        elif b[j].isdigit():
            d += 1

    if c >= 3 and d >= 1:
            e = len(b)
            if e > a:
                z = b
                a = e

if a > 0:
    print(z)
    print(a)
else:
    print("NAVERIA OUT")
