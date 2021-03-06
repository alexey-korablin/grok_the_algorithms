# - алгоритм должен быть оптимальным по времени выполнения и/или по затраченным ресурсам памяти
#
# ****************
# БИНАРНЫЙ ПОИСК |
# ****************
#
# Пример применения: поиск данных в упорядоченном списке
#
# Описание работы алгоритма:
#   -> (на вход) получает сортированный список
#   <- (на выходе) номер позиции элемента в списке или null (если ничего не найдено)
#
# При бинарном поиске всякий раз исключается половина значений из диапазона.
# Определить необходимое количество шагов можно с помощью логарифма по основанию 2.
# Логарифм считается от длинны списка в котором предполагается вести поиск. Вычислитмь количество шагов в списке, длина
# которого равна 240000 можно с помощью следующего кода:
# from math import log2, ceil
# ceil(log2(240000))
# результат 18 (так как данное число лежит в диапазоне между 2**17 и 2**18)

# Пример реализации алгоритма поиска числа в массиве

from random import randint, random
from math import ceil, log2, floor


def get_list_element(array):
    is_truly = True if random() > 0.5 else False
    if is_truly:
        elem_number = randint(0, len(array))
        return [array[elem_number], elem_number]
    else:
        return ['_', randint(len(array) + 1, len(array) * 2)]


def get_number_of_attempts(array):
    return ceil(log2(len(array)))


def process_binary_search():
    test_list = [a for a in range(12, 21)]  # -> [12, 13, 14, 15, 16, 17, 18, 19, 20]
    low = 0
    height = len(test_list) - 1
    chosen_elem, elem_number = get_list_element(test_list)
    print(chosen_elem, elem_number)
    attempt_count = 0
    expected_attempts_count = get_number_of_attempts(test_list)
    while low <= height:
        attempt_count += 1
        mid = floor((low + height) / 2)
        print('mid ->', mid)
        print('low and height ->', low, height)
        guess = test_list[mid]
        print('guess ->', guess)
        if guess == chosen_elem:
            return [mid, attempt_count, expected_attempts_count]
        elif elem_number > mid:
            low = mid + 1
        else:
            height = mid - 1
    return [None, attempt_count, expected_attempts_count]


result = process_binary_search()

print('result ->', result[0], 'attempt count ->', result[1], 'expected count of attempts ->', result[2])

# Время выполнения алгоритма. Простой перебор vs Бинарный поиск. Время выполненеия ПП - линейное: количество попыток
# равно количеству элементов (в худшем случае). БП выполняется за логарифмическое время. На 1 млрд элементов нужно не
# 1 млрд попток, а 32 (максимум)
#
# О-большое - нотация для описания скорости работы алгоритма.
# Зависимость времени выполненеия ПП от БП не линейная:
# Количество элементов |   ПП   |   БП   | БП быстрее в _ раз
# ------------------------------------------------------------
# 100                  | 100ms  | 7ms    | 15
# ------------------------------------------------------------
# 10000                | 10sec  | 14ms   | 715
# ------------------------------------------------------------
# 1000000000           | 12days | 30ms   | 34560000
#
# Запись О-большого: O(n), где n - количество операций, которые выполнит алгоритм.
# О-большое определяет время выполненеия в худшем случае
# Алгоритмы обладают двумя характеристиками времени выполненеия: худшее время и среднее время
# Скорость работы алгоритмов от быстрого к медленному:
# O(log n) - Пример: бинарный поиск
# O(n) - Пример: простой поиск
# O(n * log n) Пример: эффективные алгоритмы сортировки (ьыстрая сортировка)
# O(n**2) - Пример: медленные алгоритмы сортировки (сортировка выбором)
# O(n!) - факториальное время. Пример: очень медленные алгоритмы (Задача о коммивояжере)
