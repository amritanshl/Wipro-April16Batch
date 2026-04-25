#new_list = [expression with if condtion]
squares=[]
for x in range(10):
    squares.append(x**2)

#square_lc = [x for x in squares if x%2==0]
square_lc = [x**2 for x in range (10)]
print(square_lc)

names = ["amrit", "bob", "akshat","charlie", "ed"]
cap_names = [name.upper() for name in names  if len(name) >3]
print(cap_names)


