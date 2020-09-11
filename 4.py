# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

lang_ru = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
ru_list = []

with open('data.txt', 'r') as data:
    for i in data:
        i = i.split(' ', 1)
        ru_list.append(lang_ru[i[0]] + '  ' + i[1])

with open('data_ru.txt', 'w') as data_ru:
    ru = data_ru.writelines(ru_list)
    print(ru_list)
