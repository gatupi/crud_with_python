from flask import Flask
from flask_restful import Api, Resource
from flask import request
from flask import Response
from database import Database
import json
import json_ext
from models import Customer
from datetime import date
import str_ext

app = Flask(__name__)
api = Api(app)

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return {"msg": "hello world!"}

@app.route('/customers', methods=['GET'])
def get_customers():
    _json = json_ext.toJSON(Database.select_all_customers())
    return {"customers":json.loads(_json)}

@app.route('/customer', methods=['POST', 'PUT'])
def create_customer():
    _dict = request.get_json(force=True)

    birth_date = _dict['birth_date']
    year = int(str_ext.substr(birth_date, 6))
    month = int(str_ext.substr(birth_date, 0, 2))
    day = int(str_ext.substr(birth_date, 3, 2))

    customer = Customer(
        id = _dict['id'],
        first_name = _dict['first_name'],
        middle_name = _dict['middle_name'],
        last_name = _dict['last_name'],
        birth_date = date(year, month, day),
        phone_number = _dict['phone_number'],
        email = _dict['email'],
        gender = _dict['gender']
    )

    if request.method == 'POST':
        Database.insert_customer(customer)
    elif request.method == 'PUT':
        Database.update_customer(customer)

    return Response(status=201)

@app.route('/customer/<id>', methods=['DELETE'])
def delete_customer(id: int):
    Database.delete_customer(id)
    return Response(status=200)

if __name__ == "__main__":
    app.run(debug=True)