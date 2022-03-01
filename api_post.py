import requests
import json

url= "https://gorest.co.in/public/v2/users"
headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}
body= {
    "email":"Tugce_murat@hotmail.com",
    "name":"Tugce Murat",
    "gender":"Female",
    "status":"active"
}
result = requests.post(url,headers=headers,data=body)
print(result.status_code)
print(result.json())