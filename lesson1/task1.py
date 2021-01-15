time = int(input('Введите время в секундах'))
hour = (time // 3600)
minute = (time % 3600) // 60
second = time % 60
print(f"Результат конвертации секунд - {hour}:{minute}:{second}")