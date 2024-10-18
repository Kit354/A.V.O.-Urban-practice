def custom_write(file_name, *strings):
    strings_positions = {}
    line_number = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings[0]:
        start_of_line_byte = file.tell()
        file.write(f'{string}\n')
        line_number += 1
        strings_positions[(line_number, start_of_line_byte)] = string
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
