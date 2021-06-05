import json

import requests


def get_inventory():
  response = requests.get("http://localhost:8000")
  print(response)
  print(response.content)


get_inventory()

data = {"type": "Tulip", "colour": "red", "number": "4"}
requests.post("http://localhost:8000", json.dumps(data))

get_inventory()