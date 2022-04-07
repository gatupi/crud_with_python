import pydoc
from models import Customer
from populate import customers
from database import Database, getIndex # cuidado com nome de pasta igual ao de arquivo (mas nesse caso o problema era tentar acessar um índice de algo que não é array)
from view_models import CustomerListView
import json
import json_ext

Database.execute_dml('DELETE FROM Customer')

for customer in customers:
    Database.insert_customer(customer)

customers[2].middle_name= 'Vinicios'
customers[2].phone_number = '16991229211'
customers[2].email = 'raphael.vinicios.alonso@outlook.com'


# Database.update_customer(customers[2])
# Database.delete_customer(id=11)

result = Database.select_all_customers()
for customer in result:
    print(customer.to_string())

print(json_ext.toJSON(result))

print("Conexão bem sucedida!")