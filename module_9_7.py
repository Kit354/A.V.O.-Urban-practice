def is_prime(func):
    def wrapper(*args):
        result_func = func(*args)
        if result_func <= 1:
            return 'Составное'
        for i in range(2, int(result_func ** 0.5) + 1):
            if result_func % i == 0:
                return 'Составное'
        else:
            return 'Простое'

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
