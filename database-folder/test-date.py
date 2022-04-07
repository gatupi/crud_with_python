from datetime import date
from pickle import NONE

# date1 = date(1997,12,8)
# date2 = date(1,1,1)

# print(date1)
# print(date2)

def id(value: int):
    strval = str(value) if value != None else None
    return strval if strval != None else 'NULL'

def quote(value: str):
    return f"'{value}'" if value != None else 'NULL'

print(id(None))
print(id(12))
print(quote(None))
print(quote('Gabriel'))

number = None
strn: str = str(number)
print(f'type: {type(number)}, value: {number}')
print(f'type: {type(strn)}, value: {strn}')

values = ['Gabriel', 'Corinthians', 'Futebol', 'Testando']
print(type(values))
print(len(values))