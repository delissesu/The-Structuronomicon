# angka_random = [10000, 5000, 20000]
angka_random = list(map(int, input().strip().split()))
jumlah_sementara = 0
list_baru = []  
for i in range(len(angka_random)):
    if i == 0: list_baru.append(angka_random[0])
    else:
        jumlah_sementara += list_baru[-1] + angka_random[i]
        list_baru.append(jumlah_sementara)
        jumlah_sementara = 0
print(list_baru)