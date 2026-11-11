#FOR READING A FILE.!


f=open("demo.py","r")
data=f.read()
print(data)
f.close

f=open("demo.py")
data=f.readline()
print(data)
f.close

f=open("demo.py","r")
f.read(6)
print(data)
f.close


f=open("demo.py","r")
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
line3=f.readline()
print(line3)

# FOR OVERWRITING A FILE.!

f=open("demo.py","w")
f.write("myself surya")
f.close

# FOR READING AND REPLACING A TEXT FROM STRATING.!!

f=open("demo.py","r+")
f.write("abcefgh")
f.close

f=open("demo.py","r+")
f.write("suryajeet")
print(f.read())
f.close

with open("demo.py","r") as f:
    data=f.read()
    print(data)

with open("demo.py","w") as f:
    f.write("new data")

f=open("demo.py","r")
print(f.read())

#FOR CREATING A FILE IF NOT EXSIST AND OPENING IT FOR READING AND WRITING.

f=open("demon.py","a+")
f.write("this is suryajeet maurya from up mirzapur.")
f.close

f=open("demon.py","a+")
data=f.read()
print(data)
f.close

import os
os.remove("demon.py")


with open("demo.py","w") as f:
    f.write("HI EVERYONE THIS IS SURYAJEET MAURYA .\n we arw learning python from apna college . ")
    f.wrtite("using java .\n I like programing in java.")

with open("demo.py","r") as f:
    data=f.read()
    print(data)

with open("demo.py","r") as f:
    data=f.read()
    print(data)
new_data=data.replace("python","java")
print(new_data)

with open("demo.py","w") as f:
    f.write(new_data)

word="learning"
with open("demo.py","r"):
    data =f.read()
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")


def check_for_line():
    word="learning"
    data=True
    line_no=1
    with open("demo.py","r") as f:
        while data:
            data =f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1
check_for_line()
