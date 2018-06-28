import json
import requests

appID = '8f15d45b18dd3f64d682903a1aea784a'
mapURI = 'http://api.openweathermap.org/data/2.5'
targetCity = 'Stockholm,se'

address = (mapURI + "/weather?q=" + targetCity + "&appid=" + appID  + "&")

r=requests.get(address)

if (r.status_code == requests.codes.ok):
  print("200 OK")

