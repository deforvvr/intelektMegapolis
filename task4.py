# python

import csv

with open('history_mirror.csv', encoding="utf8") as csvfile: # открываем файл history_mirror.csv
    classes = {}  # словарь для новой информации
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')  #
    answer = list(reader)[1:]

    for row in answer:  # проходка по всему файлу и заполнение словаря
        if row[0].split('-')[0] not in classes:
            classes[row[0].split('-')[0]] = {'count': 0}
            classes[row[0].split('-')[0]]['count'] += 1

        else:
            classes[row[0].split('-')[0]]['count'] += 1

for i in classes:  # вывод данных
    count = classes[i]['count']
    print(f'В {i} году зеркало было использовано {count}.')