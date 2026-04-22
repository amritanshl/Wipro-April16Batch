import os
old_name = "D:\\Microsoft\\Microsoft\\Wipro-April16Batch\\6-file-handling\\data\\sample.txt"
new_name = "D:\\Microsoft\\Microsoft\\Wipro-April16Batch\\6-file-handling\\data\\renamed_file.txt"
try: 
    os.rename(old_name,new_name)
    os.remove(old_name)
except FileNotFoundError:
    print("File not found")
except FileExistsError:
    pass
except PermissionError:
    pass


