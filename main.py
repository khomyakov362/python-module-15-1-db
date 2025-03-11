from random import randint

import pyodbc

from db_handler import DataBaseHandler

SERVER = r'DESKTOP-OEP43AI\SQLEXPRESS'
DATABASE = 'test_1'
USERNAME = 'sa'
PASSWORD = 'ssfreSD'

# connection_string = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE=master;UID={USERNAME};PWD={PASSWORD}'

connection_string = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

generated_numbers = list(map(lambda _: randint(1, 100), range(200)))

connection = pyodbc.connect(connection_string)

db_handler = DataBaseHandler(connection)

try:

    # db_handler.create_data_base('test_1')

    # db_handler.create_number_table()

    db_handler.insert_numbers('RandomNumbers', 'Number', generated_numbers)

    num_list = db_handler.retrieve_numbers('RandomNumbers', 'Number')

    print(num_list)
except pyodbc.ProgrammingError as ex:
    print(ex)

