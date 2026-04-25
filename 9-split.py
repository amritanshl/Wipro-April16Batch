import re 
text = "python, ruby, c#, go, java, scala; pyspark, 1,2,3,4,5,6,7,8,9,10and we are going to use, these programming languages, as my primary one1,2,3,4,5,6,7,8,9,10"
nums = "1,2,3,4,5,6,7,8,9,10"
toListFormat = re.split(r"[^a-zA-Z]", text)

for wi in text:
    print(wi)
