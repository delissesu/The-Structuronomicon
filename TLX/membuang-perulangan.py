# Deskripsi
# Anda diberikan N buah bilangan. Jika ada bilangan yang diulang lebih dari satu kali, buanglah kemunculan bilangan-bilangan tersebut selain kemunculan pertama. Lalu keluarkan kembali bilangan-bilangan tersebut sesuai urutan pada masukan.

# Format Masukan
# Baris pertama berisi sebuah bilangan bulat N. N baris berikutnya berisi N buah bilangan bulat, satu buah setiap baris.

# Format Keluaran
# Beberapa baris sesuai dengan deskripsi di atas.

# Contoh Masukan
# 5
# 4
# 2
# 4
# 3
# 2
# Contoh Keluaran
# 4 
# 2 
# 3

# n_line = input()
# try:
#     n = int(n_line.strip())
# except:
#     n = 0

# output = []

# i = 0
# while i < n:
#     line = input()
#     try:
#         bil = int(line.strip())
#     except:
#         i += 1
#         continue
#     duplicate = False
#     j = 0
#     while j < len(output):
#         if output[j] == bil:
#             duplicate = True
#             break
#         j += 1
#     if not duplicate:
#         output.append(bil)
#     i += 1

# i = 0
# while i < len(output):
#     print(output[i])
#     i += 1
    
# n_line = input()
# try:
#     n = int(n_line.strip())
# except:
#     n = 0

# output = []

# i = 0
# while i < n:
#     line = input()
#     try:
#         bilangan = int(line.strip())
#     except:

# Deskripsi
# Anda diberikan N buah bilangan. Jika ada bilangan yang diulang lebih dari satu kali,
# buanglah kemunculan bilangan-bilangan tersebut selain kemunculan pertama.
# Lalu keluarkan kembali bilangan-bilangan tersebut sesuai urutan pada masukan.

jumlah_baris = int(input())

output = []

for i in range(jumlah_baris):
    n = int(input().strip())
    
    if n not in output:
        output.append(n)
            
for num in output: print(num)