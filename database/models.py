from datetime import date

class Customer:
    def __init__(self, id: int, first_name: str, last_name: str, birth_date: date, gender: str, phone_number: str, email: str, middle_name: str = None):
        self.id = id,
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.phone_number = phone_number
        self.email = email