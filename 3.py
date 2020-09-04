# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    min_num = min(num_1, num_2, num_3)
    if min_num == num_1:
        print(num_2 + num_3)
    else:
        if min_num == num_2:
            print(num_1 + num_3)
        else:
            print(num_1 + num_2)


my_func(6, 1, 2)
