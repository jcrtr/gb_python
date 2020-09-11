# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

profit = {}
pr = {}
prof = 0
prof_middle = 0
count = 0

with open('data.txt', 'r') as data:
    for i in data:
        name, own, earning, loss = i.split()
        profit[name] = int(earning) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            count += 1
    if count != 0:
        prof_middle = prof / count
        print(f'--- average_profit: {prof_middle} ---')
    else:
        print(f'Убыток')

    pr = {'average_profit': round(prof_middle)}
    profit.update(pr)
    print(f'Прибыль компаний: \n {profit}')

with open('data.json', 'w') as data_js:
    json.dump(profit, data_js)
    js_str = json.dumps([profit])
    print(f'----- json создан -----')
    print(f' {js_str}')
