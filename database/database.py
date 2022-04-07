from curses import curs_set
import email
from sqlite3 import connect
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

def id(value: int):
    f: str = id
    return f if f != None else 'NULL'

class Database:
    @staticmethod
    def insert_customer(customer: Customer):
        connection = db_connect()
        cursor = connection.cursor() # add new query to the connection
        command = f"""EXEC dbo.InsertCustomer
            {quote(customer.id)},
            {quote(customer.first_name)},
            {quote(customer.middle_name)},
            {quote(customer.last_name)},
            {quote(customer.birth_date)},
            {quote(customer.gender)},
            {quote(customer.phone_number)},
            {quote(customer.email)}
            """
        cursor.execute(command)
        cursor.commit() # dml commands require to call this method
        cursor.close()
        db_disconnect(connection)

    @staticmethod
    def update_customer(customer: Customer):
        connection = db_connect()
        cursor = connection.cursor()
        command = """EXEC dbo
        """
