N = int(input())

# baca baris pertama (A)
A = [0] * N
print(A)
i = 0
while i < N:
    A[i] = int(input().split()[0])
    # print("ini A sekarang", A)
    i += 1  
    
B = [0] * N
i = 0
while i < N:
    B[i] = int(input().split()[0])
    # print("ini B sekarang", B)
    i += 1

T = int(input())

t = 0
while t < T:
    parts = input().split()
    P = parts[0]
    x = int(parts[1])
    Q = parts[2]
    y = int(parts[3])
    
    # A 2 B 1
    
    if P == "A":
        if Q == "A":
            A[x - 1], A[y - 1] = A[y - 1], A[x - 1]
        else:
            A[x - 1], B[y - 1] = B[y - 1], A[x - 1]
    else:
        if Q == "A":    
            B[x - 1], A[y - 1] = A[y - 1], B[x - 1]
        else:
            B[x - 1], B[y - 1] = B[y - 1], B[x - 1]

    t += 1

for i in range(N):
    print(A[i], end=' ')
print()
for b in range(N):
    print(B[i], end=' ')
