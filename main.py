import requests
endpoint = ".../api/ip"
data = {"ip": "1.1.2.3"}
headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}

print(requests.post(endpoint, data=data, headers=headers).json())