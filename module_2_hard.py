def result(n):
    pole2 = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            result1 = i + j
            if i == j:
                continue
            elif result1 == n:
                pole2 += f'{i}{j}'
            elif n % result1 == 0:
                pole2 += f'{i}{j}'
    return pole2


print(result(3))
print(result(4))
print(result(5))
print(result(6))
print(result(7))
print(result(8))
print(result(9))
print(result(10))
print(result(11))
print(result(12))
print(result(13))
print(result(14))
print(result(15))
print(result(16))
print(result(17))
print(result(18))
print(result(19))
print(result(20))
