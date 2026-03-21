angka = [1, 2, 3, 4]
genap = []
ganjil = []

for i in angka:
    if i % 2 == 0: genap.append(i)
    else: ganjil.append(i)

angka.clear();print(angka)
# angka.extend(genap);angka.extend(ganjil);print(angka)
angka = genap + ganjil
print(angka)