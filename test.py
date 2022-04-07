# import requests

# BASE = "http://localhost:5000/"

# response = requests.get(BASE + "helloworld")
# print(response.json())

name = "gabriel"
for chr in name:
    print(f'{chr}')

print(len(name))
print(name[4])

name += ' alonso'
print(name)