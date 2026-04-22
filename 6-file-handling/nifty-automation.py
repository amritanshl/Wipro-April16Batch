import os
import time
from datetime import datetime

while True:
    now = datetime.now()
    #2026/
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    second = now.strftime("%S")

    target_dir = os.path.join(year,month,day,hour,minute,second)
    os.makedirs(target_dir,exist_ok=True)
    
    file_name = now.strftime("hdfc_%Y%m%d%H%M%S.txt")
    full_path = os.path.join(target_dir, file_name)

    with open(full_path, "w") as f:
        absolute_path = os.path.abspath(full_path)
        f.write(f"Log generated Date: {now.strftime("%Y-%m-%d %H:%M:%S")} \n")
        print(f"Log generated Date: {now.strftime("%Y-%m-%d %H:%M:%S")} \n")
        f.write(f"FileLocation: {absolute_path} \n")
        print(f"FileLocation: {absolute_path} \n")
    time.sleep(5)