t1 = "This is my core sentence. This is taught by Amritansh Lal."
length = len(t1)
#frequency
char_freq =  {}
toLowerF = t1.lower()
for c in toLowerF:
    if c in char_freq:
        char_freq[c] +=1
    else:
        char_freq[c] = 1
#print(char_freq)

#slicing
t2 = "programming"
def string_ends(s):
    if len(s)<2:
        return ""
    return s[:2] + s[-2:]
# print(string_ends(t2))
# print(string_ends("hey "))

t3 = "proper popping ping poster" #3
# pro3er 3o33ing 3ing 3oster
modify_str = t3[0]+t3[1:].replace(t3[0], "__")
# print(modify_str)

str1 = "parrot"
str2= "peacock"
#paacock , perrot
new_str = str2[:2] +str1[2:] + " , "+ str1[:2] + str2[2:]
# print(new_str)

t4 ="bounce"
t5 = "facing"
t6 = "ed"
def get_str (s):
    if len(s) >=3:
        if s.endswith('ing'):
            s+= 'ly'
        
        else:
            s += 'ing'
    return s

# print(get_str(t4))
# print(get_str(t5))
# print(get_str(t6))

t7 =  'The lyrics is not that poor and I am doing awesome!' #good
snot= t7.find('not')
spoor = t7.find('poor')
if spoor>snot and snot >0 and spoor >0:
    t7 = t7.replace(t7[snot:(spoor+4)], "good")
    #t8 =  t7[:snot] + "good" + t7[spoor+5:]


    # print(t7)
    # print(t8)

str_11="This is a Test"
# print(len(str_1))
str_1 = str_11.split()
res = []
# print(str_1[::-1])
for w  in str_1:
    if len(w)%4==0:
        reverse_it=""
        for c in w:
            reverse_it = c + reverse_it
        res.append(reverse_it)
    else:
        res.append(w)
fina_sentence = " ".join(res)
print(fina_sentence)


    
t5= ["ayush", "raj"]
new_t5 = t5[0].replace(t5[0][:2],t5[1][:2])
new_t6 = t5[1].replace(t5[1][:2],t5[0][:2])



t5= ["ayush", "raj"]#ay , ra
new_t5 = t5[0][:2].replace(t5[0][:2],t5[1][:2])#y
new_t6 = t5[1][:2].replace(t5[1][:2],t5[0][:2])#y
print("dd")

def get_mid(cont1, w):
    middle= len(cont1)//2+1
    res = cont1[:middle] + w + cont1[middle:]
    return res

print(get_mid("((((((((((())))))))))", "Amritansh"))