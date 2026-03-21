
count = 2
def fibonacci(numberOne : int, numberTwo : int) -> int:
    global count
    if count <= 19:
        newFibo = numberTwo + numberTwo
        print(newFibo)
        number_one = numberOne
        number_two = newFibo
        count += 1
        fibonacci(number_one, number_two)
    else:
        return -1
    
    return -1


fibonacci(0, 1)
