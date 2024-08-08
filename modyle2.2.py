first = int(input('Введите число: '))
second = int(input('Введите число: '))
third = int(input('Введите число: '))
if first % 3 == 0 and second % 5 == 0 and third % 6 == 0:
    print('3')
elif first % 3 == 0 and second % 5 == 0:
    print('2')
elif second % 5 == 0 and third % 6 == 0:
    print('2')
elif first % 3 == 0 and third % 6 == 0:
    print('2')
else:
    print('0')
