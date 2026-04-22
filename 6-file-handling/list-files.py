import os

path = "."#. also represent current working directory



items = os.listdir(path)
for item in items:
    if os.path.isdir(item):
        print(f"{item} is a directory [DIR]")
        child_dir = os.chdir(os.path.join(path,item))
        print(f"{child_dir} exists in {item}")

    else: 
       # print(f"{item}  is a file [FILE]")
       pass