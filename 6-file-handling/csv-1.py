import csv
# data = [
#     [
#         "Account_No","Customer_Name","Balance","City"
#     ],
#     [
#         106,"Amritansh Lal", 50000.99, "Banglore"
#     ]
# ]
# with open('hdfc_customer.csv',"w",newline='') as f:
#     write_it = csv.writer(f)
#     write_it.writerows(data)
with open('hdfc_customer.csv',"r") as f:
    reader = csv.reader(f)
    next(reader)
    # count = sum(1 for row in reader)
    # print(f"Total records: {count}")
    
    for row in reader:
        if float(row[2])>10000.00:
            pass
           # print(f"High Balance : {row[0]} - {row[1]} with balance : {row[2]}")
#Append
new_record = [107, 'Amritansh Lal', 200000, 'Bengaluru']
with open ('hdfc_customer.csv', 'a', newline='') as d:
    # writer = csv.writer(d)
    # writer.writerow(new_record)
    pass


#to dictionary
with open ('hdfc_customer.csv', 'r') as d:
    reader = csv.DictReader(d)
    for row in reader:
       # print(row)
       pass

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


headers = [
    "emp_id",
    "name",
    "age",
    "salary",
    "email",
    "is_active",
    "hobbies",   
    "present_street",
    "present_city",
    "present_state",
    "present_zip_code",
    "permanent_street",
    "permanent_city",
    "permanent_state",
    "permanent_zip_code"
]

#print(user_profile.items())

with open('employee_profiles.csv','w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()

    for emp_id, info in user_profile.items():
        row = {
            "emp_id": emp_id,
            "name": info["name"],
            "age": info["age"],
    "salary": info["salary"],
    "email": info["email"],
    "is_active": info["is_active"],
    "hobbies": info["hobbies"],
    "present_street": info["address"]["presentAddress"]["street"],
    "present_city": info["address"]["presentAddress"]["city"],
    "present_state": info["address"]["presentAddress"]["state"],
    "present_zip_code": info["address"]["presentAddress"]["zip_code"],
    "permanent_street": info["address"]["permanentAddress"]["street"],
    "permanent_city": info["address"]["permanentAddress"]["city"],
    "permanent_state": info["address"]["permanentAddress"]["state"],
    "permanent_zip_code": info["address"]["permanentAddress"]["zip_code"]
    }
        writer.writerow(row)