import os

current_location = os.getcwd()
print(current_location)

my_file =os.path.join(current_location,"sample_folder")

print(my_file)

if os.path.exists(my_file):
    os.rmdir(my_file)
    print("it exists")
else:
    os.mkdir(my_file)