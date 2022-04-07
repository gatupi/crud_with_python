import pyodbc
from models import Customer

def db_connect():
    server = 'localhost,1433'
    database = 'Commerce'
    username = 'sa'
    password = '$TupiSQLSERVER2022'
    str_conn = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    return pyodbc.connect(str_conn)

def db_disconnect(connection):
    connection.close()

def quote(value: str):
    return f"'{value}'" if value != None else 'NULL'

def number(value):
    strval = str(value) if value != None else None
    return strval if strval != None else 'NULL'

class Database:
    @staticmethod
    def execute_dml(command: str):
        connection = db_connect()
        cursor = connection.cursor() # add new query to the connection
        cursor.execute(command)
        cursor.commit() # dml commands require to call this method
        cursor.close()
        db_disconnect(connection)

    @staticmethod
    def insert_customer(customer: Customer):
        command = f"""EXEC dbo.InsertCustomer
            {number(customer.id)},
            {quote(customer.first_name)},
            {quote(customer.middle_name)},
            {quote(customer.last_name)},
            {quote(customer.birth_date)},
            {quote(customer.gender)},
            {quote(customer.phone_number)},
            {quote(customer.email)}
            """
        print(command)
        Database.execute_dml(command)

    @staticmethod
    def update_customer(customer: Customer):
        command = f"""EXEC dbo.UpdateCustomer
            {number(customer.id)},
            {quote(customer.first_name)},
            {quote(customer.middle_name)},
            {quote(customer.last_name)},
            {quote(customer.birth_date)},
            {quote(customer.gender)},
            {quote(customer.phone_number)},
            {quote(customer.email)}
        """
        print(command)
        Database.execute_dml(command)
