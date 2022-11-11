def russian_peasant_multiplication(x,y):
    right = []
    left = []
    while y != 1:
        right.append(x)
        left.append(y)
        if y%2 == 0:
            right.pop(x)
            left.pop(y)
        x = x*2
        y = y//2
    return sum
