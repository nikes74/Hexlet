# Интерполяция

# Вам даны три переменные с фамилиями разных людей: one, two, three.
# Составьте и выведите на экран слово из символов в таком порядке:
#
# Третий символ из первой строки
# Второй символ из второй строки
# Четвертый символ из третьей строки
# Пятый символ из второй строки
# Третий символ из второй строки
# Попробуйте использовать интерполяцию. Внутри фигурных скобок можно размещать не только переменные, но и отдельные
# символы строки, извлеченные по индексу (с помощью квадратных скобок).

one = 'Naharis'
two = 'Mormont'
three = 'Sand'

# BEGIN (write your solution here)
word = one[2] + two[1] + three[3] + two[4] + two[2]
print(word)
# END

# teacher
# print(f'{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}')
