import requests

url= "https://gorest.co.in/public/v2/users/2436"
headers = {'Authorization': 'Bearer a102bd6582f80eb0b2a7e6cce8b7ecbe4b35f7ddf8fade9225f6e6d279a4ee20'}

result = requests.delete(url,headers=headers)
print(result.status_code)
