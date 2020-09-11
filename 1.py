# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

data = open('data.txt', 'w')
text = input('Введите текст: \n')


def text_w(text):
    data.writelines(text + '\n')


def text_r():
    data = open('data.txt', 'r')
    content = data.readlines()
    print(content)
    data.close()


while text:
    text_w(text)
    text = input('Введите текст: \n')
    if not text:
        data.close()
        break

text_r()
