# Алгоритм Дейкстры
# Алгоритм Дейкстры помогает найти самый быстрый путь.
# АД состоит из 4-х шагов:
#   1) Найти узел с наименьшей стоимостью
#   2) Обновить стоимость соседей этого узла
#   3) Повторить для всех узлов
#   4) Вычислить итоговый путь
# При вычислении стоимости берется в расчет стоимость достижения узлов 1-го уровня. Время достижения конечного узла
# считается бесконечным
# Поиск ближайших соседей с наименьшей стоимостью достижения происходит также как и при поиске соседей 1-го уровня. При
# нахождении более короткого пути до заданного узла следует обновить его стоимость
# АД для конечного узла не применяется
# При раблоте с АД с каждым ребром связывается число называемое "весом"
# "Взвешенным графом" называют граф с весами
# "Невзвешенный граф" - граф без весов
#
# Граф может содержать циклы. В этом случае поиск начинается и заканчивается узлом "А"
# Каждый обход цикла уваеличивает вес на вес путей задействованных в цикле. Путь через цикл НИКОГДА не будет кратчайшим.
# Частный случай цикла - ненаправленный граф (граф в котором узлы указывают друг на друга)
# АД работает ТОЛЬКО с направленными ациклическими графами (DAG - Directed Acyclic Graph)
# АД не умеет работать с отрицательными весами! Для работы с такими графами существует алгоритм Беллмана - Форда


def graph_search():
    infinity = float('inf')
    shortest_path = []
    graph = dict()
    # graph['me'] = ['alice', 'bob', 'claire']
    graph['start'] = {}
    graph['start']['a'] = 6
    graph['start']['b'] = 2
    print(graph['start'].keys())
    print(graph['start']['a'])
    graph['a'] = {}
    graph['a']['fin'] = 1
    graph['b'] = {}
    graph['b']['a'] = 3
    graph['b']['fin'] = 5
    graph['fin'] = {}

    costs = dict()
    costs['a'] = 6
    costs['b'] = 2
    costs['fin'] = infinity

    parents = dict()
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = None

    processed = []

    def find_lowest_cost_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        print('lowest cost node ', lowest_cost_node)
        return lowest_cost_node

    node = find_lowest_cost_node(costs)

    while node is not None:
        shortest_path.append(node)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    print(processed)
    return shortest_path


print(graph_search())

# Признаки NP-полной задачи:
#   * алгоритм замедляется при увеличении количества элементов
#   * формулировка "все комбинации Х"
#   * необходимость вычислять все варианты Х и задачу невозможно разбить на подзадачи
#   * если просматривается некоторая последовательность и нет простого решения
#   * если есть некоторое множество и нет простого решения
# .