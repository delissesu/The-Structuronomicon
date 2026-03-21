# data = list(map(int, input().split()))
# tanggal = data[0]
# bulan = data[1]
# tahun = data[2]

# sum_tanggal = 0
# while tanggal > 0:
#     sum_tanggal += tanggal % 10
#     tanggal //= 10

# sum_bulan = 0
# while bulan > 0:
#     sum_bulan += bulan % 10
#     bulan //= 10

# sum_tahun = 0
# while tahun > 0:
#     sum_tahun += tahun % 10
#     tahun //= 10

# total = sum_tanggal + sum_bulan + sum_tahun

# if total != 11 and total != 22 and total != 33:
#     while total > 9:
#         temp = 0
#         while total > 0:
#             temp += total % 10
#             total //= 10
#         total = temp

# print(total)

simpan = input().split()
print(simpan)
lifepath = [1,2,3,4,5,6,7,8,9,11,22,33]
total = []
for i in simpan:
    temp = 0
    for j in i:
        print(j)
        temp+= int(j)
        print("ini temp", temp)
    while temp not in lifepath:
        print("ini juga temp", temp)
        x = str(temp)
        temp = 0
        for k in x:
            print(k)
            temp+=int(k)
            print(temp)
    total.append(temp)

hasil = 0
for i in total:
    hasil += i 
print(hasil)

while hasil not in lifepath:
    x = str(hasil)
    hasil=0
    for i in x:
        hasil+=int(i)

print(hasil)