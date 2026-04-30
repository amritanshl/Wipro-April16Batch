d1= {0: 10, 1: 20}
d1[2]=30
# print(d1)

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
res = {}
res.update(dic1)
res.update(dic2)
res.update(dic3)
# print(res)
if 60 == dic3[6]:
    pass
else:
    pass

for k,v in res.items():
   pass# print(f"Key : {k} -- Values {v}")

n = 5
my_dict={}
for a in range(1,n+1):
    my_dict[a]= a*a
# print(my_dict)

k = 3
number = [10,1,2,3,4,5,6,7]
nums = sorted(list(set(number))) #ascending
print(nums)
print(nums[k-1])
print(nums[-k])
