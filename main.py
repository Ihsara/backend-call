import requests
import json

with open('.env_var.json') as envfile:
    env_var = json.load(envfile)

with open('instance.json') as datafile:
    data = json.load(datafile)
endpoint = env_var['address']
headers = {"Authorization": env_var['token']}

print(data)

print(requests.post(endpoint, json=data, headers=headers).json())