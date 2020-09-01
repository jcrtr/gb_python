# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

input_list = str(input('Введите слова через пробел:')).split(' ')

number = 0
count_list = len(input_list)
count = 1

while True:
    if count <= count_list:
        first = input_list[number][:10]
        number += 1
        print(f'{count}: {first}')
        count += 1
    else:
        break
