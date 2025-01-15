import requests

headerdata={"T1":"Firstname", "T2":"LastName"}
url = "https://httpbin.org/get"
responce = requests.get(url,headers=headerdata)
print(responce.text)
