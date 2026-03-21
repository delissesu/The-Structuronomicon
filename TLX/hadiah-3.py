# angka = 5
# pangkat = 3
# temp = 1
# hasil = 0

# for _ in range(pangkat):
#     temp = temp * angka
# hasil += temp
# print(hasil)

N = int(input())
hadiah = []
pangkat = 0
while N > 0:
    if N % 3 == 1:
        hadiah.append(3**pangkat)
    N //= 3
    pangkat += 1

print(len(hadiah))
print(*hadiah)