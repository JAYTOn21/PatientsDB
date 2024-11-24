from workWithDB import create_query
from dataImport import create_insert, data, title, conn, worksheet
import re

Errors = ['']


def get_data(id_patient, value, connection, name_table, sheet, all_table):
    global Errors
    number = id_patient + 1  # Получение ид пациента для удобства
    number = str(number)
    row = [id_patient]

    ind = 0
    while True:
        # Тупо работа с данными из Excel
        liter = value[ind]

        cell = liter + number
        data_cell = sheet[cell].value
        # Работа с исключительными данными
        if data_cell is None:
            data_cell = 'Null'
        if data_cell == '-':
            data_cell = '0'
        if data_cell == '+':
            data_cell = '1'
        if re.findall(r'[a-zA-Zа-яА-Я]', str(data_cell)):
            data_cell = f"'{data_cell}'"

        row.append(data_cell)

        ind += 1
        # Обычные выходы из цикла
        if liter == value[-1]:
            break
        if liter == 'AV':
            print('Error: Отсутствует данное значение в таблице')
            break

    # Создание запроса и его заполнение в БД
    print("Создание и отправление запроса для таблицы " + name_table)
    query = create_insert(name_table, row, all_table)
    create_query(connection, query)
    mes = create_query(connection, f"SELECT * FROM mydb.{name_table}")
    # Проверка на запись в сервере
    ind = list(mes[-1])
    ind = int(str(ind[0]))      # Преобразование ID пациента в запросе из кортежа в INT
    if ind != id_patient and id_patient > 1 and name_table == all_table[0]:
        print(f"Ошибка при заполнении таблицы {name_table} пациента номер {str(id_patient)}")
        print(f"Последняя запись: {mes[-1]}")
        # print(f"Отправленный запрос: {query}")
        if Errors[-1] != id_patient:
            print("Добавлена новая ошибка в список")
            Errors.append(id_patient)
        else:
            print("Повторная ошибка")
    # print("Таблица " + name_table + " успешно заполнена.\n")


def write():
    for i in range(2, 128):      # 347 в первом цикле - количество людей
        print("\n\nПациент номер " + str(i))
        table = title[0]
        get_data(i, data[table], conn, table, worksheet, title)


write()
print(Errors)
print(f"Количество неудачных запросов на заполнение БД: {len(Errors)-1}")
