# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

data = open('data.txt', 'r')

content = data.readlines()
print(f'--- Колличество строк в файле: {len(content)} ---')

for i in range(len(content)):
    print(f'{len(content[i])} - символов в строке: {i + 1}')

data.close()
