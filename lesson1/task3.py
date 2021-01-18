a = input('Введите положительное целое число')
i = 0
j = 0
while i <= len(a) - 1:
    if int(a[i]) > j:
        j = int(a[i])
    i += 1
print(f'Самая большая цифра в числе - {j} ')
