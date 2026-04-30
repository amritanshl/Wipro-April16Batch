import json

json_data = '{"name": "amrit","sub":"CSE", "Age": 27 }'

python_obj = json.loads(json_data)
print(f"Name: {python_obj["name"]}" )

user_profile = {
    "emp001": {
    "name": "John Doe",#string
    "age": 30,#integer
    "salary": 75000.00,#float
    "email": "john.doe.example.com",#string
    "is_active": True,#boolean
    "hobbies": ["reading", "traveling", "coding"],#list
    "address": {#dictionary
        "presentAddress": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA",
            "zip_code": "12345"
        }
    ,
        "permanentAddress": {
            "street": "456 Elm St",
            "city": "NYC",
            "state": "NY",
            "zip_code": "67890"
        }
    }   
    }, 
    "emp002": {
    "name": "Jane Smith",   
    "age": 28,
    "salary": 68000.00,
    "email": "jane.smith.example.com",
    "is_active": False,
    "hobbies": ["painting", "hiking", "cooking"],
    "address": {
        "presentAddress": {
            "street": "789 Oak St",
            "city": "Sometown",
            "state": "TX",
            "zip_code": "54321"
        },
        "permanentAddress": {
            "street": "321 Pine St",
            "city": "LA",
            "state": "CA",
            "zip_code": "98765"
        }
    }
    }
}

json_sstring = json.dumps(user_profile, sort_keys=True, indent=4)
# print(json_sstring)
sampleList = ['abc', 'xyz', 'aba', '1221', "samsungs", "appa", "cadnium", "dog", "elaphant", "eggs"]
count = 0
for w in sampleList:
    if (len(w)>2 and w[0] == w[-1]):
        count +=1

# print(count)
listt = [[2,3,56],[88,3243,7675]]

# import itertools
# perms = list(itertools.permutations(sampleList))

# print(perms)

for a in listt:
    if isinstance(a, list):
        print(a)

ls0= ['p', 'q']
n = 5
ress =[]

for i in range(1, n+1):
    for j in ls0:
        ress.append(f"{j}{i}")

print(ress)