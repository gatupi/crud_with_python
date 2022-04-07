import pyodbc
from models import Customer
from view_models import CustomerListView

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

def getIndex(array: list, value):
    count = 0
    while count < len(array):
        if array[count] == value:
            return count
        count += 1

class Database:
    @staticmethod
    def execute_dml(command: str):
        connection = db_connect()
        cursor = connection.cursor() # add new query to the connection
        cursor.execute(command)
        cursor.commit() # dml commands require to call this method
        cursor.close()
        db_disconnect(connection)

    def execute_select(command: str):
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(command)
        columns = [column[0] for column in cursor.description]
        values = cursor.fetchall()
        cursor.close()
        db_disconnect(connection)
        return {
            "columns": columns,
            "values": values
        }

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
        Database.execute_dml(command)

    @staticmethod
    def delete_customer(id: int):
        command = f"EXEC dbo.DeleteCustomer {number(id)}"
        Database.execute_dml(command)

    @staticmethod
    def select_all_customers():
        command = f"SELECT * FROM dbo.SelectAllCustomers"
        dict = Database.execute_select(command)
        columns = dict['columns']
        ls = []
        for val in dict['values']:
            ls.append(CustomerListView(
                val[getIndex(columns, 'Id')],
                val[getIndex(columns, 'Name')],
                val[getIndex(columns, 'BirthDate')],
                val[getIndex(columns, 'Age')],
                val[getIndex(columns, 'PhoneNumber')],
                val[getIndex(columns, 'Email')]
            ))

        return ls