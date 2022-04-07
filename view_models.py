import json

class CustomerListView:
    def __init__(self, id: int, name: str, birth_date: str, age: int, phone_number: str, email: str):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.age = age
        self.phone_number = phone_number
        self.email = email

    def to_string(self):
        return f"Id: {self.id}\nName: {self.name}\nDate of birth: {self.birth_date} ({self.age} yo)\nPhone number: {self.phone_number}\nEmail: {self.email}\n"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)