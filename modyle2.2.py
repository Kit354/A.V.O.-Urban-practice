first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first % 2 == 0 == second % 5 == 0 == third % 6 == 0 == first % 3 == 0:  # Если ввести к примеру 432-325-3426
    print('3')
elif first % 3 == 0 == second % 5 == 0:
    print('2')
elif second % 5 == 0 == third % 6 == 0:
    print('2')
elif first % 3 == 0 == third % 6 == 0:
    print('2')
else:
    print('0')
