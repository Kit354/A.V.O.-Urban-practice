import os
import time

print('Текущая директория: ', os.getcwd())
for root, dirs, files in os.walk('.'):
    for file in files:
        filepath = os.path.join('.', file)
        filetime = os.path.getmtime(f'{file}')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(f'{file}')
        parent_dir = os.path.dirname(f'{dirs}')
        print(
            f'Обнаружен файл: {file}, '
            f'Путь: {filepath}, '
            f'Размер: {filesize} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
