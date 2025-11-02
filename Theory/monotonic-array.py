ex_array = [8, 6, 10, 2]

for i in range(len(ex_array) - 1):
    p = ex_array[i + 1]
    p2 = ex_array[i]
    
    if (p >= p2) or (p <= p2) : 
        print("True")
    else:
        print("Else")