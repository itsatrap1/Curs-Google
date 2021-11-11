# TEMA 2
suma = 0


def integer_sum(*args) -> int:
    global suma
    arg_list = args
    if len(arg_list) == 0:
        return 0
    for item in arg_list:
        t = str(type(item))
        suma += item if t.find('int') != -1 else 0
    return suma


def recursive_sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)


def sum_of_even(n: int) -> int:
    if n <= 0:
        return 0
    if not n % 2 == 0:
        return sum_of_even(n-1)
    else:
        return n + sum_of_even(n-2)


def sum_of_odd(n: int) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return sum_of_odd(n-1)
    else:
        return n + sum_of_odd(n-2)


def ret_int(number) -> str:
    t = str(type(number))
    if t.find('int') != -1:
        msg = 'Este numar intreg'
        return msg
    else:
        return '0'


print('Suma este {0}'.format(integer_sum(1, 'a', -2, [10, 20], 3, 10)))
print(integer_sum())

print('Suma este {0}'.format(recursive_sum(10)))
print('Suma numerelor pare este {0}'.format(sum_of_even(10)))
print('Suma numerelor impare este {0}'.format(sum_of_odd(5)))
print(ret_int(2))
print(ret_int(1.5))
