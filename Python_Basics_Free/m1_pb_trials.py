# 1 # Инвертированный регистр  Испытание пройдено
# 2 # Вращение троек  Испытание пройдено
# 3 # Степени тройки  Испытание пройдено
# 4 # Идеальные числа
# 5 # Физзбазз  Испытание пройдено
# 6 # Классификация отрезков
def is_degenerated(section) -> bool:
    (x1, y1), (x2, y2) = section

    # if x1 == x2 and y1 == y2:
    #     result = True
    # else:
    #     result = False
    # return result
    return x1 == x2 and y1 == y2


def is_vertical(section) -> bool:
    (x1, y1), (x2, y2) = section

    return x1 == x2 and y1 != y2


def is_horizontal(section) -> bool:
    (x1, y1), (x2, y2) = section

    return x1 != x2 and y1 == y2


def is_inclined(section) -> bool:
    (x1, y1), (x2, y2) = section
    return x1 != x2 and y1 != y2

line = (0, 10), (100, 130)
# print(is_degenerated(line))

# 7 # Счастливый билет
def is_happy_ticket(number: str) -> bool:
    size = len(number)
    first_half, second_half = 0, 0
    for i in range(size):
        if i >= size // 2:
            second_half += int(number[i])
        else:
            first_half += int(number[i])

    # Alternative
    # middle = len(number) // 2
    # first_half, second_half = 0, 0
    # for i in range(middle):
    #     second_half += int(number[i + middle])
    #     first_half += int(number[i])
    return True if first_half == second_half else False
# print(is_happy_ticket('128506'))

# 8 # Сумма двоичных чисел
# 9 # Счастливые числа
# 10 # Шифрование
def encrypt(message: str) -> str:
    size = len(message)
    last_char = ''
    pairs_chars = []
    swap_pairs = []
    for i in range(size // 2):
        pair = message[i * 2:i * 2 + 2]
        pairs_chars.append(pair)
        swap_pairs.append(pair[1] + pair[0])
    if size % 2 != 0:
        last_char = message[-1]
    pairs_chars.append(last_char)
    swap_pairs.append(last_char)

    return pairs_chars, ''.join(swap_pairs)

print(encrypt('attack!'))

# 11 # Фасад
# 12 # Фибоначчи  Испытание пройдено
def fib(n: int) -> int:  # Числа Фибоначчи
    f = [0, 1]
    summ = 0
    if n > 0 and n >= 2:  # для положительных чисел Фибоначчи
        for i in range(2, n + 1):
            summ = f[i - 1] + f[i - 2]
            f.append(summ)
    return f[n]
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711,
# 0, 1, 2, 3, 4, 5, 6,  7,  8,  9, 10, 11,  12,  13,  14,  15,  16,   17,   18,   19,   20,    21,    22,

# 13 # Разница углов




