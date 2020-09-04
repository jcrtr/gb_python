# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = str(input('Имя: '))
surname = str(input('Фамилия: '))
year = int(input('Год рождения: '))
city = str(input('Город проживания: '))
email = str(input('Email: '))
phone = int(input('Телефон: '))


def user(name, surname, year, city, email, phone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {year}, Город проживания: {city}, Email: {email}, Телефон: {phone}')


user(name=name, surname=surname, year=year, city=city, email=email, phone=phone)
