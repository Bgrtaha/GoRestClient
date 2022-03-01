import requests
import json

url= "https://gorest.co.in/public/v2/users/2435"
headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}
body= {
    "email":"bugra_murat@hotmail.com",
    "name":"Bugra avcı",
    "gender":"male",
    "status":"active"
}
result = requests.patch(url,headers=headers,data=body)
print(result.status_code)
print(result.json())