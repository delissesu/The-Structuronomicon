angka: int = int(input())

prima : bool = True

for i in range(2, angka):
    if angka % i == 0:prima = False
print(prima)

faktor : int = 2
while faktor <= (angka - 1):
    if angka % faktor == 0:
        prima = False
        break
    else: faktor += 1

print(prima)