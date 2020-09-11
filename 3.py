# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('data.txt', 'r') as data:
    middle = []
    min_user = []
    content = data.read().split('\n')
    for i in content:
        i = i.split()
        if int(i[1]) < 20000:
            min_user.append(i[0])
        middle.append(i[1])

print(f'Средний оклад равен: {sum(map(int, middle)) / len(middle)}')
print(f'Список людей с окладом меньше 20.000: {min_user}')
