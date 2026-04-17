thisTuple = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape")
print(thisTuple)  # Output: ('apple', 'banana', 'cherry')
print(type(thisTuple))  # Output: <class 'tuple'>
print(thisTuple[0])  # Output: apple
print(thisTuple[1:4])  # Output: ('banana', 'cherry', 'date')
print(thisTuple[:3])  # Output: ('apple', 'banana', 'cherry )
converList = list(thisTuple)
print(converList)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
converList[1] = "blueberry"
converList.append("honeydew")
converList.insert(2, "kiwi")
print(converList)  # Output: ['apple', 'blueberry', 'kiwi', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
newTuple = tuple(converList)

constantTupleMensuration = (3.14, 2.718, 1.618)
#unpacking tuple
pi, e, phi = constantTupleMensuration

print(pi)  # Output: 3.14
print(e)  # Output: 2.718
print(phi)  # Output: 1.618
#unpacking tuple
fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7, fruit8, fruit9 = newTuple

