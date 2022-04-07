from datetime import date
from models import Customer

customers = [
    Customer(
        first_name = "Gabriel",
        middle_name = "Willian",
        last_name = "Alonso",
        birth_date = date(1997,12,8),
        gender = "M",
        phone_number = "16991229305",
        email = "gabriel.tupi.alonso@gmail.com"
    ),
    Customer(
        first_name = "Raphael",
        last_name = "Alonso",
        birth_date = date(1999,3,28),
        gender = "M",
        phone_number = "16991229305",
        email = "raphael.alonso@gmail.com"
    ),
    Customer(
        first_name = "Mariana",
        middle_name = "Beatriz",
        last_name = "Malaguti",
        birth_date = date(2002,5,30),
        gender = "F",
        phone_number = "16991229305",
        email = "mariana.malaguti@gmail.com"
    ),
    Customer(
        first_name = "Aline",
        last_name = "Capocci",
        birth_date = date(1980,5,18),
        gender = "F",
        phone_number = "16991229305",
        email = "aline.capocci@gmail.com"
    )
]