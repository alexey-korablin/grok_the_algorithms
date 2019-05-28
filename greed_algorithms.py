#!/usr/bin/env python

# ЖАДНЫЙ АЛГОРИТМЫ
# Жадные алгоритмы просты.
# ЖА на каждом шаге выбирает оптимальный вариант. Или так: на каждом шаге выбирается локально-оптимальное решение, что
# на выходе дает глобально-оптимальное решение
# ЖА далеко не всегда работает оптимально, но зачастую результат близок к оптимальному, а неточность вычислений может
# быть скомпенсирована простотой алгоритма
#
# Приближенный алгоритм - вид ЖА. Применяется когда вычисление точного результата занимает слишком много времени. Его
# эффективность оценивается по быстроте и близости полученного результата к оптимальному


def find_best_station():
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['mt', 'wa', 'id'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            print('27 -> ', station, states_for_station)
            covered = states_for_station & states_needed
            print('29 -> ', covered)
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

            print('34 -> ', best_station, states_covered)
        states_needed -= states_covered
        final_stations.add(best_station)
    return final_stations


print(find_best_station())

# Время выполнения ЖА - O(n**2)
# Признаки NP-полной задачи:
#   * алгоритм замедляется при увеличении количества элементов
#   * формулировка "все комбинации Х"
#   * необходимость вычислять все варианты Х и задачу невозможно разбить на подзадачи
#   * если просматривается некоторая последовательность и нет простого решения
#   * если есть некоторое множество и нет простого решения
# .