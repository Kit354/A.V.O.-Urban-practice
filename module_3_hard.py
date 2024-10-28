# def calculate_structure_sum(structure):
#     for i in structure:
#         if isinstance(i, list):
#             return 0
#         return 1 + calculate_structure_sum(structure[1:])
#
#
#
# data_structure = [1, 2, 3]
#
# result = calculate_structure_sum(data_structure)
# print(result)

# def calculate_structure_sum(data):
#     total_sum = 0
#     total_length = 0
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if isinstance(key, str):
#                 total_length += len(key)
#             value_sum, value_length = calculate_structure_sum(value)  # Рекурсия
#             total_sum += value_sum
#             total_length += value_length
#     elif isinstance(data, list) or isinstance(data, tuple):
#         for item in data:
#             item_sum, item_length = calculate_structure_sum(item)  # Рекурсия
#             total_sum += item_sum
#             total_length += item_length
#     elif isinstance(data, str):
#         total_length += len(data)
#     elif isinstance(data, (int, float)):
#         total_sum += data
#     return total_sum, total_length
#
#
# # Входные данные
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
#
# # Вычисление суммы
# total_sum, total_length = calculate_structure_sum(data_structure)
# result = total_sum + total_length  # Итоговая сумма
# print(result)  # Ожидаемый вывод: 99


# Рабочий на половину
# def calculate_structure_sum(item):
#     total_sum = 0
#     if isinstance(item, list):
#         for i in item:
#             suma = calculate_structure_sum(i)  # Рекурсия
#             total_sum += suma
#     elif isinstance(item, tuple):
#         for i in item:
#             suma1 = calculate_structure_sum(i)  # Рекурсия
#             total_sum += suma1
#     elif isinstance(item, dict):
#         for key, value in item.items():
#             suma_key = calculate_structure_sum(key)  # Рекурсия
#             suma_value = calculate_structure_sum(value)
#             total_sum += suma_key
#             total_sum += suma_value
#     if isinstance(item, str):
#         total_sum += len(item)
#     elif isinstance(item, (int, float)):
#         total_sum += item
#     return total_sum
#
#
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
#     ]
#
# result = calculate_structure_sum(data_structure)
# print(result)


def calculate_structure_sum(*item):
    total_sum = 0
    for i in item:
        if isinstance(i, list):
            suma = calculate_structure_sum(*i)  # Рекурсия
            total_sum += suma
        elif isinstance(i, tuple):
            suma1 = calculate_structure_sum(*i)  # Рекурсия
            total_sum += suma1
        elif isinstance(i, set):
            suma1 = calculate_structure_sum(*i)  # Рекурсия
            total_sum += suma1
        elif isinstance(i, dict):
            for key, value in i.items():
                suma_key = calculate_structure_sum(key)  # Рекурсия
                suma_value = calculate_structure_sum(value)
                total_sum += suma_key
                total_sum += suma_value
        if isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (int, float)):
            total_sum += i
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

result = calculate_structure_sum(data_structure)
print(result)
