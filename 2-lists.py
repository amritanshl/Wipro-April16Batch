thisList = ["apple", "banana", "cherry"]
print(len(thisList))  # Output: 3
list1 = [1, 2, 3, "four", "five", True, False, None, [1, 2, 3], {"key": "value"}, (1, 2, 3)]
print(list1)  # Output: [1, 2, 3, 'four', 'five', True, False, None, [1, 2, 3],{"key": "value" }]

#roll numbe - interger, name - string, is_student - boolean, grades - list, info - dictionary, coordinates - tuple
profileList = [12345, "John Doe", True, [85, 90, 92], {"age": 20, "major": "Computer Science"}, (40.7128, -74.0060)]

print(profileList[-3:-1])  # Output: [[85, 90, 92], {'age': 20, 'major': 'Computer Science'}]
print(profileList)  # Output: [12345, 'John Doe', True, [85, 90, 92], {'age': 20, 'major': 'Computer Science'}, (40.7128, -74.0060)]
print(type(thisList))  # Output: <class 'list'>
#list() constructor
newList = list(("apple", "banana", "cherry"))
print(newList)  # Output: ['apple', 'banana', 'cherry']
print(profileList[3])  # Output: [85, 90, 92]
print(profileList[3][1])  # Output: 90
print(profileList[-1])  # Output: (40.7128, -74.0060)
#[start:end] specific range of items
print(profileList[1:4])  # Output: ['John Doe', True, [85, 90, 92]]
# from start to end
print(profileList[:4])  # Output: [12345, 'John Doe', True, [85, 90, 92]]
studentMarksof10Inorder = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#get top 3 marks
print(studentMarksof10Inorder[:3])  # Output: [10, 9, 8]

# to the end
print(studentMarksof10Inorder[3:])  # Output: [7, 6, 5, 4, 3, 2, 1]
#negative indexing
print(studentMarksof10Inorder[-3:-1])  # Output: [3, 2]
data = [12345, 'Mary Doe', True, [85, 90, 92], {'age': 20}, (40.7128, -74.0060)]
print(data[-3:])  # Output: [[85, 90, 92], {'age': 20}, (40.7128, -74.0060)]

#update name in profileList
profileList[1] = "Mary Doe"
print(profileList)  # Output: [12345, 'Mary Doe', True, [85, 90, 92], {'age': 20, 'major': 'Computer Science'}, (40.7128, -74.0060)]

#update age name and is_student in profileList
profileList[1:3] = ["Alice Smith", False]
print(profileList)  # Output: [12345, 'Alice Smith', False, [85, 90, 92], {'age': 20, 'major': 'Computer Science'}, (40.7128, -74.0060)]

# new car list
carList = ["Toyota", "Honda", "Ford", "BMW", "Audi"]
# add "Mercedes" at index 2
carList.insert(2, "Mercedes")
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'Ford', 'BMW', 'Audi']
#replace "Ford" with "Tesla"
carList[3] = "Tesla"
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'Tesla', 'BMW', 'Audi']
#append "Lexus" to the end of the list
carList.append("Lexus")
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'Tesla', 'BMW', 'Audi', 'Lexus']
carList.insert(len(carList), "Volkswagen")
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'Tesla', 'BMW', 'Audi', 'Lexus', 'Volkswagen']
#create American car list
americanCars = ["Ford", "Chevrolet", "Tesla", "Dodge", "Jeep"]
newcarList = carList.extend(americanCars)
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'Tesla', 'BMW', 'Audi', 'Lexus', 'Volkswagen', 'Ford', 'Chevrolet', 'Tesla', 'Dodge', 'Jeep']
newcarList.remove("Tesla")
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'BMW', 'Audi', 'Lexus', 'Volkswagen', 'Ford', 'Chevrolet', 'Dodge', 'Jeep']  
#use pop() to remove the last item from the list
carList.pop()   
print(carList)  # Output: ['Toyota', 'Honda', 'Mercedes', 'BMW', 'Audi', 'Lexus', 'Volkswagen', 'Ford', 'Chevrolet', 'Dodge']                   

# carList.clear()  # Clear all items from the list
# print(carList)  # Output: []

