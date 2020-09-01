# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


elements = list(input('Введите значение: '))
count = 0

for i in range(len(elements) // 2):
    elements[count], elements[count + 1] = elements[count + 1], elements[count]
    count += 2

items = ''.join(elements)
print(f'{items}')
