import requests
import json

URL = "http://127.0.0.1:8000/empdata/"


def Get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    # print(json_data)
    r = requests.get(url=URL)
    data2 = r.json()
    print(data2)


Get_data(1)


def Post_data():
    data = {
        'id': 1,
        'Name': 'Ashitosh',
        'Salary': 15000,
        'Description': 'Java developer',
        'Designation': 'ASE',
        'Manager': 'Ritu'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data2 = r.json()
    print(data2)


# Post_data()
