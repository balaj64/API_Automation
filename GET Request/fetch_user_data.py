import requests
import jsonpath

url="https://reqres.in/api/users?page=2"

# Send request
response = requests.get(url)
json_result=response.json()
json_path=jsonpath.jsonpath(json_result,"data")
print(response.status_code)
assert response.status_code == 200

# print(json_path)
print(json_result)
for i in range(len(json_result["data"])):
    # json_path=jsonpath.jsonpath(json_result,"data["+str(i)+"].id")
    # print(json_path)
    result=json_result["data"][i]["avatar"]
    print(result)

# Fetch Header
print(response.headers)
print(response.encoding)
print(response.cookies)
print(response.headers.get("Report-To"))

