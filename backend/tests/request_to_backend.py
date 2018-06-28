#!/usr/bin/python3

import json
import requests

r = requests.get('http://localhost:9000/api/weather')

if (r.status_code == requests.codes.ok):
  print("200 OK")

dict1 = json.loads(r.text)

if ('icon' in dict1.keys()):
  print("Icon detected..")
