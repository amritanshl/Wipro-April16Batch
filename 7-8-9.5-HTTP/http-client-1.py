import http.client, json
#https://dogapi.dog/api/v2/breeds
#conn = http.client.HTTPConnection("127.0.0.1", 8000)
host = "dogapi.dog"
conn=http.client.HTTPSConnection(host)

path = "/api/v2/breeds"
conn.putrequest("GET", path)
conn.putheader("Accept","application/json")
conn.endheaders()

response = conn.getresponse()
print(f"Server Response: {response.status} - {response.reason}")

full_data= []
print("-------------Data Streaming Started-------------")
while True:
    chunk = response.read(256)
    if not chunk:
        break
    full_data.append(chunk.decode('utf-8'))
    print(f"Received chunk : {len(chunk)} bytes")

complete_body  = "".join(full_data)
#print(complete_body)
if response.status==200:
    json_payload = json.loads(complete_body)
    print(json_payload)
else:
    print("not found")