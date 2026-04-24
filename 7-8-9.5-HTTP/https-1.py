import requests, httpx
import json
from urllib.parse import urlparse, parse_qs

client = requests.Session()

client_response =client.get('https://dogapi.dog/api/v2/breeds')

parsed_url = urlparse('https://dogapi.dog/api/v2/breeds/f9643a80-af1d-422a-9f15-18d466822053')
print(f"scheme: {parsed_url.scheme}")
print(f"path : {parsed_url.path}")
response = requests.get('https://dogapi.dog/api/v2/breeds')

if response.status_code ==200:
    with open("sample.json", "w") as f:
    
        json.dump(client_response.json(), f, indent=4)
       # f.write(response.text)
        print(f"status code is {response.status_code}")
else:
    print(f"status code is {response.status_code}")

import requests, json

targer_url = "http://127.0.0.1:8000/tasks/5"
response = requests.get(targer_url)
print(f"Response is : {response.content}")
print(f"Status Code is : {response.status_code}")
print(f"Content Type is : {response.headers.get('Content-Type')}")
print(f"Response is : {response.content}")

if response.status_code == 200:
    with open("pass.json", "w") as f:
        json.dump(response.json(), f, indent=4)
else: 
    with open("fail.json", "w") as f:
        json.dump(response.json(), f, indent=4)