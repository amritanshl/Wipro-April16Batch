thisset = {"apple", "banana", "cherry"}
print(thisset)  # Output: {'apple', 'banana', 'cherry'}
print(type(thisset))  # Output: <class 'set'>
thisset.add("orange")  # Add an item to the set
print(thisset)  # Output: {'apple', 'banana', 'cherry', 'orange'}
thisset.add("cherry")  # Add an item to the set
print(thisset)  # Output: {'apple', 'banana', 'cherry', 'orange'}

thisset.remove("banana")  # Remove an item from the set

#Boolean paradox: True and 1 are considered equal, as are False and 0. Therefore, when you add both True and 1 to a set, only one of them will be stored because sets do not allow duplicate values. The same applies to False and 0.
secondSet ={True, False, 1, 0, "True", "False"}
print(secondSet)  # Output: {False, True, 0, 1, 'True', 'False'}
thirdSet = {"amrit", 1, True, 1.5, "amrit"}
print(thirdSet)  # Output: {1.5, 'amrit', 1, True}
fourthSet = {"amrit", False,0}
print(fourthSet)  # Output: {False, 'amrit', 0}

#remove, discard, pop, clear
fourthSet.remove("amrit")  # Remove an item from the set
print(fourthSet)  # Output: {False, 0}

fourthSet.discard("amrit")  # Remove an item from the set if it exists
print(fourthSet)  # Output: {False, 0}

fourthSet.pop()  # Remove and return an arbitrary item from the set
print(fourthSet)  # Output: {0} or {False} (since sets are unordered, the item removed by pop() can be any item from the set)

fourthSet.clear()  # Remove all items from the set
print(fourthSet)  # Output: set()

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}
#Union of sets
unionSet = setA.union(setB)
print(unionSet)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
#Intersection of sets
intersectionSet = setA.intersection(setB)
print(intersectionSet)  # Output: {4, 5}
#Difference of sets
differenceSet = setA.difference(setB)       
print(differenceSet)  # Output: {1, 2, 3}
differenceSet2 = setB.difference(setA)
print(differenceSet2)  # Output: {6, 7, 8}


