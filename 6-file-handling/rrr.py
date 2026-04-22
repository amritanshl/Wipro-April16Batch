with open("D:\\Microsoft\\Microsoft\\Wipro-April16Batch\\6-file-handling\\data\\sample.txt", "r") as file:
    content = file.read()
    print("1-----------")
    print(content)

with open("D:\\Microsoft\\Microsoft\\Wipro-April16Batch\\6-file-handling\\data\\readline_example.txt", "r") as file:
    content_1 = file.readline()
    content_se = file.readline()
    content_th = file.readline()
    print("2-----------")
    print(content_1)
    print(content_se)
    print(content_th)

with open("D:\\Microsoft\\Microsoft\\Wipro-April16Batch\\6-file-handling\\data\\readlineS_ example.txt", "r") as file:
    print("3-----------")
    content_2 = file.readlines()
    for lines in content_2:
        print(lines.replace("o","#######AMRIT#######"))
