import json
import requests
import pprint

url = 'http://httpbin.org/post'
data = {"data" : "24.3"}
data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
requests.post()

print(response.status_code)
pprint.pprint(response.json())
