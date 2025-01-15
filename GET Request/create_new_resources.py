import json

import requests


url="https://reqres.in/api/users"

json_file="C:/Users/HP/Downloads/file.json"
with open (json_file,'r') as file:
    json_input=file.read()
    request_json=json.loads(json_input)

print(request_json)

responce=requests.post(url,json=request_json)
print(responce.status_code)
print(responce.text)
print(responce.headers.get('Content-Type'))

# retrive the data
Id=responce.json()
print(Id["createdAt"])
