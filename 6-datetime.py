from datetime import datetime

now = datetime.now()
mylogtime = "2026/04/22 09:21"
timestamp = now.strftime("%Y-%m-%d__%H-%M-%S-%A")
timestamp2 = now.strptime(mylogtime,"%Y/%m/%d %H:%M")
print(timestamp)
print(timestamp2)
