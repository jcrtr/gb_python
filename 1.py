num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))


def division(num_1, num_2):
    div = num_1 / num_2
    print(f'- Ответ равен: {div}')


if num_2 <= 0:
    print('----- На 0 делить нельзя! -----')
else:
    division(num_1, num_2)
