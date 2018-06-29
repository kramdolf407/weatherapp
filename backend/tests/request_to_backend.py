import json
import requests

r = requests.get('http://localhost:9000/api/weather')

if (r.status_code == requests.codes.ok):
  print("*******")
  print("200 OK")
  print("*******")

dict1 = json.loads(r.text)

print(dict1)

if ('icon' in dict1.keys()):
  print("*******")
  print("Icon detected..")
  print("*******")
