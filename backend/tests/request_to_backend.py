import json
import requests

r = requests.get('http://localhost:9000/api/weather')

if (r.status_code == requests.codes.ok):
    print("-------")
    print("Backend site responded with 200 OK")
    print("-------")

dict1 = json.loads(r.text)

if ('icon' in dict1.keys()):
    print("Icon detected..")
