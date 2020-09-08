# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

import random
answer_list = []


def answer():
    list_random = [random.randint(0, 200) for i in range(10)]
    for i in range(1, len(list_random)):
        if list_random[i] > list_random[i - 1]:
            answer_list.append(list_random[i])
    return answer_list


answer_new = answer()

print(f'Список чисел: {answer_new}')

