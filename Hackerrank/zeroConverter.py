def pos(n):
    if n == 0:
        print('already Zero')
    else:
    ## Write the code
        while n > 0:
            n -= 1
            print(n, end=' ')

def neg(n):
    if n == 0:
        print('already Zero')
    else:
        while n <= 0:  # Ubah kondisi untuk include 0
            print(n, end=' ')
            n += 1
            if n > 0:  # Stop setelah print 0
                break

def pos1(n):
    if n == 0:
        print('already Zero')
    else:
        while n > 0:
            n -= 1
            print(n, end=' ')

def neg1(n):
    if n == 0:
        print('already Zero')
    else:
        while n <= 0:
            print(n, end=' ')
            if n == 0:  # Stop setelah print 0
                break
            n += 1
            
def pos2(n):
    if n == 0:
        print('already Zero')
    else:
        for i in range(n-1, -1, -1):
            print(i, end=' ')

def neg2(n):
    if n == 0:
        print('already Zero')
    else:
        for i in range(n, 1):
            print(i, end=' ')