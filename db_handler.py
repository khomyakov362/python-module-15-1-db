from pyodbc import Cursor, Connection

class DataBaseHandler:

    def __init__(self, connection : Connection):
        self._connection = connection
        self._cursor = self._connection.cursor()
    
    @property
    def cursor(self):
        return self._cursor
    
    def create_data_base(self, data_base_name : str):
        existing_value = self._connection.autocommit
        self._connection.autocommit = True
        self.cursor.execute(f'CREATE DATABASE {data_base_name};')
        self._connection.autocommit = existing_value
    
    def create_number_table(self):
        self.cursor.execute(f'''CREATE TABLE dbo.RandomNumbers 
(
    Id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    Number INT NOT NULL
);''')
        self.cursor.commit()

    def insert_numbers(self, table_name : str, column : str, list_of_num : list[int]):

        formatted_numbers = ','.join(map(lambda el: f'({el})', list_of_num))
        
        self.cursor.execute(f'''INSERT INTO {table_name} ({column})
VALUES {formatted_numbers}''')

        self.cursor.commit()
    
    def retrieve_numbers(self, table_name : str, column : str) -> list[int]:
        self.cursor.execute(f'''SELECT {column}
FROM {table_name}''')

        rows = self.cursor.fetchall()

        flat_list = [item for row in rows for item in row]

        return flat_list
        