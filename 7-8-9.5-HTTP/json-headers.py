import requests

new_hire = {
    "name":"Amritansh",
    "department": "Database Dep",
    "role":"SDE"
}
#-----------------------------------------------
import json
manual_response = requests.post(
    "urls",
    data=json.dumps(new_hire),
    headers={
        "Content-Type":"application/json",#Encoding response 415, 406
        "Accept": "application/json"#Decoding  406
    }

)