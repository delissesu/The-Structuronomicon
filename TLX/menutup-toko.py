# luas = [
#     [225 * 335, 299 * 278, 300 * 250],
#     [215 * 394, 144 * 718, 300 * 290],
#     [200 * 400, 240 * 333, 142 * 619],  
#     [314 * 298, 411 * 198, 333 * 222]
# ] 

# harga_jual = [100, 120, 150]
# nh = len(harga_jual)
# nl = len(luas)

# for merek in range(nh):
#     total = 0
#     for toko in range(nl):
#         total += luas[toko][merek] * harga_jual[merek]
    
#     print(total)
    
# for row in luas:
#     print(row, row[0], row[1])

# print()
# for i in range(nl):
#     print(luas[i], luas[0])

brands = [
    [(225,335), (215,394), (200,400), (314,298)],  # merek 1
    [(299,278), (144,718), (240,333), (411,198)],  # merek 2
    [(300,250), (300,290), (142,619), (333,222)],  # merek 3
]

prices = [100, 120, 150]

# for i in range(3):
#     total = 0
#     for w, h in brands[i]:
#         # print(f"ini {w} dan ini {h}")
#         total += w * h * prices[i]
#         # print(w, h)
#     print(total)

# tupleNum = (1, 2, 3)
# print(tupleNum[0]);print(tupleNum[1]);print(tupleNum[2])
    
# brands[0] = [(225,335), (215,394), (200,400), (314,298)]
for pasangan in range(len(brands)):
    
    total = 0
    
    print("Ini adalah elemen per baris:")
    print(brands[pasangan])
    for value in brands[pasangan]:
        p1 = value[0]
        p2 = value[1]
        
        total += (p1 * p2) * prices[pasangan]
        # print(value)
        print(p1, p2)
    print(total)
    print()