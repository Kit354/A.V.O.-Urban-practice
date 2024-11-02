def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        result_function = function(int_list)
        result[function.__name__] = result_function
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
