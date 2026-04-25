# class Countdown:
#     def __init__(self,start):
#         self.current = start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current <=0:
#             raise StopIteration
#         value = self.current
#         self.current -=1
#         return value
    
# counter = Countdown(3)
# for x in counter:
#     print(x)

def countdown_generator(n):
    while n>0:
        yield n
        n -=1
nums = countdown_generator(3)
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
