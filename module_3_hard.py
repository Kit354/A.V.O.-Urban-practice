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
