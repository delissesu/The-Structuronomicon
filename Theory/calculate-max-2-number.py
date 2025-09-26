list_angka : list[int] = list(map(int, input().strip().split()))

n : int = len(list_angka)
angka_maksimum : int = list_angka[0] + list_angka[1]

for i in range(n - 1):
    angka_pengganti : int = list_angka[i] + list_angka[i + 1]
    print("ini angka pengganti", angka_pengganti)
    print("ini angka maksimum", angka_maksimum)
    if angka_pengganti > angka_maksimum: angka_maksimum = angka_pengganti
print(angka_maksimum)