angka_di_list : list[int] = list(map(int, input().strip().split()))
total_penjumlahan_angka : int = 0
counter : int = 1

while counter <= len(angka_di_list):
    total_penjumlahan_angka += angka_di_list[counter - 1]
    counter += 1

print(total_penjumlahan_angka)
