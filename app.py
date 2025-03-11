import pyodbc

SERVER = r'DESKTOP-OEP43AI\SQLEXPRESS'
DATABASE = 'master'
USERNAME = 'sa'
PASSWORD = 'ssfreSD'

connection_string = f'DRIVER={{SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

connection = pyodbc.connect(connection_string)
