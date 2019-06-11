# 1 Бинарное дерево
# Поиск, вставка и удаление в бинарном дереве производится за время O(logN)
# Бинарное дерево представляет собой ветви упорядоченных списков
# Недостатки бинарных деревьем поиска:
#   нет поддержки произвольного доступа к элементам
#   время выполнения поиска сильно зависит от сбалансированности дерева. В несбалансированном дереве поиск производится
#       долго
# Использование: базы данных
# Дальнейшее чтение по теме:
#   в-деревья
#   красно-черные деревья
#   кучи
#   скошенные (splay) деревья
#
# 2 Инвертированные индексы
# Струткура даннах представляющая из себя хеш-таблицу в которой признак связан с объектом, хранящим признаки. Например
# веб-страница - является объектом, а слова на ней - признаками. При поиске страницы с определнными словами будет
# использован хеш. В выдачу попадут те страницы, которые содерджат признак
# Использование: поисковые системы
#
# 3 Преобразование Фурье
# Объяснение математической основы алгоритма может быть найдена на сейте Better Explained
# Например: преобразование Фурье может показать из каких ингредиентов он состоит или разделить песню на составляющие
# частоты
# Применение: сжатие и преобразование медиа-данных, прогнозирвование змлетрясений, анализ ДНК, поиск целого по фрагменту
#
# 4 Параллельные алгоритмы
# Позволяют существенно ускорить работу существующих алгоритмов за счет одновременного выполенния их в нескольких
# потоках
# Выигрыш во времени при использовании таких алгоритмов не линеен из-за накладных расходов на организацию параллельных
# вычислений и последующе объединение обработанных данных и из-за неравномерности распределения нагрузки
#
# 5 MapReduce
# Разновидность параллельного алгоритма. Это вид распределенных алгоритмов
# Данный алгоритм может выполнятся на множестве машин
# Пример Apache Hadoop
# Он полезен когда приходится работать с БД хранящими миллиарды записей. MySQL не сможет справиться со сложным запросом
# к такой БД, Hadoop справится превосходно
# В основе MapReduce лежат две идеи: функция отображения - map и функция свертки - reduce
# Функция map получает массив и применяет функцию к каждому его элементу
# Пример:   arr1 = [1, 2, 3, 4, 5]
#           arr2 = map(lambda x: x * 2, arr1)
#       --> [2, 4, 6, 8, 10]
# В параллельных алгоритмах map распределяет нагрузку по множеству машин
# Функция reduce - сворачивает массив до одного элемента
# Пример:   arr1 = [1, 2, 3, 4, 5]
#           reduce(lambda x, y: x + y, arr1)
#        --> 15
#
# 6 Фильтры Блума и HyperLogLog
# Предназначен для работы с очень большим объемом данных. Для поиска в таких объемах мог бы помочь хеш, со временем
# поиска в нем O(1), но в этом случае он был бы огромных размеров. Данная пробелма решается с помощью фильтров Блума
# ФБ представляют собой вероятностные структуры данных. Ответ который дают ФБ может оказаться ложным с небольшой
# вероятностью
# При использовании ФБ возможны ложно-положительные срабатывания, но исключены ложно-отрицательные
# ФБ очень компактны
# HyperLogLog - действует примерно так же. Он аппроксимирует количество уникальных элементов в множестве
#
# 7 Алгоритмы SHA
# Данный алгоритм получает строки и возвращает хеш-код этой строки
# Алгоритм SHA - это хеш-функция
# Применение: сравнение файлов, проверка паролей.
# Алгоритм SHA является локально нечувствительным. То есть при изменении всего одного символа в строке изменится вся
# строка, возвращаемая алгоритмом. Это позволяет усложнить задачу подбора пароля. Когда же нужен обратный результат,
# используется алгоритм simhash
# Simhash - алгоритм который при минимальных изменениях исходной строки возвращает минимально измененный хеш
# Полезен при выявлении дубликатов в процессе индексирования, полезен при проверке на плагиат
#
# 8 Обмен ключами Диффи - Хеллмана
# Алгоритм Диффи - Хеллмана эффективно решает задачу шифрования. При использовании алгортма ни одна из сторон не знает
# шифр -> его не нужно согласовывать; расшифровать зашифрованное сообщение чрезвычайно сложно
# АДХ использует два ключа: открытый и закрытый. Открытый ключ используется для выполненеия шифрования и может быть
# разделен между требуемым количеством сторон. Закрытый ключ хранится только у одной стороны и используется для
# дешифровки
# Применение: в алгоритме RSA
#
# 9 Линейное программирование
# ЛП использует симплекс-метод
# Применяется в областях особенно требующих оптимизации.
