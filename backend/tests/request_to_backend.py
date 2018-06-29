import json
import requests

r = requests.get('http://localhost:9000/api/weather')

if (r.status_code == requests.codes.ok):
  print("*******")
  print("200 OK")
  print("*******")


print("Do we get content??")
print(r.headers)

dict1 = json.loads(r.text)

if ('icon' in dict1.keys()):
  print("*******")
  print("Icon detected..")
  print("*******")


print("end python script")
