from workWithDB import create_connection, create_query
import openpyxl

conn = create_connection('localhost', 'root', '2173', 'mydb')
file = openpyxl.load_workbook('data.xlsx')
worksheet = file['Лист1']

# Работа с кортежами после получения списка всех таблиц
red = create_query(conn, "SHOW TABLES")

title = ['patients']

data = {title[0]: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK',
                   'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 'AU']}


def create_insert(name_table, row, tables):
    if name_table == tables[0]:    # 0
        query = f"""INSERT INTO patients VALUES
        ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, 
        {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, 
        {row[21]}, {row[22]}, {row[23]}, {row[24]}, {row[25]}, {row[26]}, {row[27]}, {row[28]}, {row[29]}, {row[30]},
        {row[31]}, {row[32]}, {row[33]}, {row[34]}, {row[35]}, {row[36]}, {row[37]}, {row[38]}, {row[39]}, {row[40]},
        {row[41]}, {row[42]}, {row[43]}, {row[44]}, {row[45]}, {row[46]}, {row[47]})"""
    return query
