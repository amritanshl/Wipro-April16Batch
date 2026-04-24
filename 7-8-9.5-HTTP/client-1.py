import requests

BASE_URL = "http://127.0.0.1:8000"
response = requests.get(f"{BASE_URL}/tasks")

new_task = {"item": "Custom item", "completed": False}
response = requests.post(f"{BASE_URL}/tasks",json=new_task)
response = requests.get(f"{BASE_URL}/tasks")
#print(response.json())

full_update = {"item":"first exaple of PUT request", "completed":True}
response = requests.put(f"{BASE_URL}/tasks/2",json=full_update  )
response = requests.get(f"{BASE_URL}/tasks")
#print(response.json())

partial_update = {"completed":False}
response = requests.patch(f"{BASE_URL}/tasks/2",json=partial_update  )
response = requests.get(f"{BASE_URL}/tasks")
print(response.json())