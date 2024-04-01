# python


import csv  # импорт для работы с файлами формата .csv

with open('history_mirror.csv', encoding='utf-8') as f:  # считываем данные из таблицы history_mirror.csv
    reader = csv.reader(f, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    result = []

    for row in answer:  # записываем удовлетворяющие условию данные в массив, в указанном в условии формате, для двльнейшего заполнения новой таблицы
        if row[2] == 'Победа над смертью':
            result.append([row[0], row[1]])

            print(f'Сообщение было зафиксировано: {row[0]} у пользователя {row[1].split()[0]} {row[1].split()[1][0]}.{row[1].split()[2][0]}.')

with open('mirror_error.csv', 'w', newline='', encoding='utf-8') as file: # создаем новую таблицу с отфильтрованными данными
    w = csv.writer(file)
    w.writerow(['date', 'username'])
    w.writerows(result)
