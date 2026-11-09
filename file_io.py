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




