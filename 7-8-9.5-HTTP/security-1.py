import requests
from requests.auth import HTTPBasicAuth

response = requests.get("http://127.0.0.1:8000/" ,auth=HTTPBasicAuth('admin', 'adminpass'))


api_token = "thisismysampletookentobeadded1112345"
headers = {
    "Authorization": f"Bearer {api_token}",
    "Accept": "application/json"
}