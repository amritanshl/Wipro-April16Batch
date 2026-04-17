#Example List
mylist = ["apple", "banana", "cherry"]
mylist.append("orange") #Add an item to the end of the list
print(mylist) #Output: ['apple', 'banana', 'cherry', 'orange']
mylist.insert(1, "grape") #Insert an item at a specific index
print(mylist) #Output: ['apple', 'grape', 'banana', 'cherry', 'orange']
mylist.remove("banana") #Remove an item by value
print(mylist) #Output: ['apple', 'grape', 'cherry', 'orange']

#Example Tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple) #Output: ('apple', 'banana', 'cherry')
mytuple[1] = "grape" #This will raise a TypeError because tuples are immutable

#Example Set
myset = {"apple", "banana", "cherry"}
myset.add("orange") #Add an item to the set
myset.add("cherry") #Add an item to the set
print(myset) #Output: {'apple', 'banana', 'cherry', 'orange'}
myset.remove("banana") #Remove an item from the set 
print(myset) #Output: {'apple', 'cherry', 'orange'}

#Example Dictionary
mydict = {
            "name": "Alice", 
            "age": 30, 
            "city": "New York"
            
            }
print(mydict) #Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

mydict["age"] = 31 #Update the value of an existing key

print(mydict) #Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}
mydict["country"] = "USA" #Add a new key-value pair
print(mydict) #Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
mydict.pop("city") #Remove a key-value pair by key