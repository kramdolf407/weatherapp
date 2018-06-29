import json
import requests
import sys

r = requests.get('http://localhost:9000/api/weather')

if (r.status_code == requests.codes.ok):
    print("-------")
    print("Backend site responded with 200 OK")
    print("-------")

else:
    print("Backend site did NOT respond with 200 OK, exiting..")
    sys.exit(1)

dict1 = json.loads(r.text)

if ('icon' in dict1.keys()):
    print("Icon detected..")
else:
    print("Icon value was not detected in JSON response. exiting..")
    sys.exit(1)
