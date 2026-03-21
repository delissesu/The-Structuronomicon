num = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Cara 1: Menggunakan nested loop dengan indeks
print("Cara 1:")
for i in range(len(num)):
    for j in range(len(num[i])):
        if j == len(num[i]) - 1:
            print(num[i][j])

# Cara 2: Menggunakan indeks -1
print("\nCara 2:")
for i in range(len(num)):
    print(num[i][-1])

# Cara 3: Menggunakan for-each loop
print("\nCara 3:")
for row in num:
    print(row[0])
    print(row[-1])

# Cara 4: Menggunakan enumerate
print("\nCara 4:")
for idx, row in enumerate(num):
    print(idx, row[-1])