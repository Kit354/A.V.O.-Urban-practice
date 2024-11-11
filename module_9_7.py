def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        if result_func % 2:
            return 'Простое'
        else:
            return 'Составное'

    return wrapper


@is_prime
def sum_three(*args):
    sum_result = 0
    for i in args:
        sum_result += i
    print(sum_result)
    return sum_result


result = sum_three(2, 3, 6)
print(result)
