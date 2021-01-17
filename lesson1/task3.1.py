a, r = int(input('Введите положительное целое число')), -1
while a > 10:
    b = a % 10
    a //= 10
    if b > r:
        r = b
print(r)
