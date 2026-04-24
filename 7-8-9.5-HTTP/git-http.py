import requests

url = "https://api.github.com/users/octocat"
response = requests.get(url)

print(response.text)
print("-------------------------------------------------------------------------\n")
print(response.json()['login'])

# #-------------------------------------------------------------------------
# import http.client, json
# conn = http.client.HTTPSConnection("api.github.com")
# headers = {"User-Agent": "Awesome-Octocat-App"}
# conn.request("GET", "/users/octocat",headers=headers)
# res = conn.getresponse()
# raw_data =res.read().decode("utf-8")
# data = json.loads(raw_data)
# print(data)

