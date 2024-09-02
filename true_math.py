from math import inf


def divide(first, second):
    if second == 0:
        return inf
    elif first / second:
        result = first / second
        return result


divide(49, 7)
divide(15, 0)
