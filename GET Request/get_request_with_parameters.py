import requests

params= {"name":"Bala","email":"balamech@gmail.com"}
url =  "https://httpbin.org/get"
responce=requests.get(url,params=params)
result=responce.text
print(result)
