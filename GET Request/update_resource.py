import json

import requests

url="https://reqres.in/api/users/2"

path="C:/Users/HP/Downloads/file.json"
file=open(path,'r')
read_file=file.read()
json_result=json.loads(read_file)

responce=requests.put(url,json=json_result)
print(responce.status_code)
json_formet=responce.json()
name=json_formet['name']
print(name)