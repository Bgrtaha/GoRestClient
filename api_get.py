import requests
import json

result = requests.get("https://gorest.co.in/public/v2/users")
print(result)
result = json.loads(result.text)

for i in result:
    print(i)
