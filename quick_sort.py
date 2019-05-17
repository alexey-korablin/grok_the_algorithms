# ********************
# БЫСТРАЯ СОРТИРОВКА |
# ********************
#
# не сортировка


def sum(arr):
    result = 0
    if len(arr) < 2:
        return result if len(arr) == 0 else arr[0]
    else:
        result = arr[0]
        del arr[0]
        return result + sum(arr)


# print(sum([8, 2, 7, 1]))


def find_max(arr):
    max_num = 0
    if len(arr) < 2:
        return max_num if len(arr) == 0 else arr[0]
    elif max_num < arr[0]:
        max_num = arr[0]
        del arr[0]
        current = find_max(arr)
        return max_num if max_num > current else current


# print(find_max([8, 3, 13, 17, 45]))


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(lesser) + [pivot] + quicksort(greater)


# print(quicksort([1, 2, 0, 2, 1, 4, 0, 5, 2, 0, 1, 9, 1, 3]))

# Скорость работы алгоритмов от быстрого к медленному:
#   БЫСТРАЯ СОРТИРОВКА O(n * log(n)) --> СОРТИРОВКА ВЫБОРОМ O(n**2)
# В сравнении со всеми изученными алгоритмами:
#   Бинарный поиск --> Линейный поиск --> Быстрая сортировка --> Сортировка выбором --> Задача о коммивояжере
from time import sleep


def quicksort2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot_index = int(len(arr) / 2)
        pivot = arr[pivot_index]
        lesser = [i for i in arr[:pivot_index] if i <= pivot] + [i for i in arr[pivot_index + 1:] if i <= pivot]
        greater = [i for i in arr[:pivot_index] if i > pivot] + [i for i in arr[pivot_index + 1:] if i > pivot]
        return quicksort2(lesser) + [pivot] + quicksort2(greater)


print(quicksort2([1, 2, 0, 2, 1, 4, 0, 5, 2, 0, 1, 9, 1, 3]))
# .