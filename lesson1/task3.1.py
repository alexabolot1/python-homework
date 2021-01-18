a = int(input('Введите положительное целое число'))
r = - 1
if a > 10:
    while a > 10:
        b = a % 10
        a //= 10
        if b > r:
            r = b
    print(r)
else:
    print(a)
