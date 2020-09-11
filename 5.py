# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random


def int_input():
    """Создание файла с вводом чисел от пользователя"""
    try:
        with open('data.txt', 'w+') as data:
            numbers = (input('Введите цифры через пробел: '))
            data.writelines(numbers)
            num = numbers.split()
            print(f'Сумма: {sum(map(int, num))}')
    except ValueError:
        print('Ошибка')


def random_numbers():
    """Рандом 15 чисел от 1 до 100"""
    numbers = [random.randint(1, 100) for i in range(15)]
    return (str(numbers)[1:-1]).replace(',', '')


def int_random():
    """Создание файла с 15 рандомными числами"""
    try:
        with open('data_random.txt', 'w+') as data_random:
            list_random = random_numbers()
            data_random.writelines(list_random)
            num = list_random.split()
            print(f'Сумма: {sum(map(int, num))}')
    except ValueError:
        print('Ошибка')


int_input()
int_random()

