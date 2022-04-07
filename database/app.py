from models import Customer
from populate import customers
from database import Database

for customer in customers:
    Database.insert_customer(customer)

print("Conexão bem sucedida!")