suhu = [10, 12, 8, 9, 15, 6]
# [1, 3, 1, 1, 0, 0]
hari = [0 for _ in range(len(suhu))]
n = len(suhu)

for i in range(n - 1):
    for j in range(i + 1, n):   
        if suhu[j] > suhu[i]:
            hari[i] = j - i
            break
print(hari)


# for i in range(len(suhu)):
#     counter = 0
#     for j in range(i, len(suhu) - 1):
#         print("ini i ke", i, "dan ini je ke", j)
#         print("ini suhu saat ini", suhu[j])
#         if suhu[j + 1] > suhu[j]:
#             counter += 1
#             hari.append(counter)
#             print("ini hari", hari)
#             break
#         else:
#             print("masuk blok else")
#             if suhu[j + 1] < suhu[j]:
#                 print('tes')
#                 print("cek counter", counter)
#                 counter += 1
#                 hari.append(counter)
#                 print("sebelum ditambah", hari)
#                 hari[-1] += counter
#                 print("setelah ditambah", hari)
#                 print("ini hari indeks terakhir", hari[-1])
#                 print(counter)
#             else:
#                 counter += 1
#                 hari[-1] += counter
#                 break

# print(hari)

# for i in range(len(suhu) - 1):
#     for j in range(i + 1, len(suhu)):
#         if suhu[j] > suhu[i]:
#             hari[i] = j - i
#             break
# print(hari)