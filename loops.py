#LOOPS ARE USED TO REPEAT A BLOCK OF INSTRUCTIONS.

COUNT=1
while COUNT<=5:
    print("HELLO WORLD!",COUNT)
    COUNT+=1

i=1
while i<=5:
    print(i)
    i+=1


i=1
while i<=10:
    print(3*i)
    i+=1


n=input("enter a number:")
i=1
while i<=10:
    print(n,"*",i,"=",int(n)*i)
    i+=1


n=int(input("enter a number:"))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

nums=[1,2,3,4,5,6,7,8,9]
idx=0
while idx<=len(nums)-1:
    print(nums,idx)
    idx+=1

nums=[1,2,5,48,3,4,5,9,7]
x=48
i=0
while i<len(nums):
    if (nums[i]==x):
        print("found at index:",i)
    else:
        print("not found.")
    i+=1

i=1
while i<10:
    print(i)
    if(i==5):
        break
    i+=1

i=1
while i<10:
    if(i==5):
        i+=1
        continue
    print(i)
    i+=1


# **FOR LOOP**

nums =[1,2,3,4,5,6,7,89,9]
for el in nums:
    print(el)

str="SURYAJEET"
for nu in str:
    print(nu)

str="surya"
for char in str:
    if char=="r":
        break
    print(char)    

str="surya"
for char in str:
    if char =="u":
        continue
    print(char)

dtr="surya"
for char in dtr:
    if char=="y":
        print("found y",char)
        continue
    else:
        print("not fond",char)


nums=(1,2,58,4,5,7,8,6,58)
x=58
idx=0
for el in nums:
    if el==x:
        print("no. found at idx:",idx)
        continue

    idx+=1

# RANGE FUNCTION!!

seq=range(5)
for i in seq:
    print(i)

seq=range(5,10)
for i in seq:
    print(i,"SMS")

SURYA=range(5,20,2)
for i in SURYA:
    print(i,"SURYAJEET")

for i in range(0,100,5):
    if i==40:
        print(i,"SURYAJEET")
        break
    else:
        print("not found")

n=int(input("enter a number:"))
for i in range(1,11):
    print(n*i)

# PASS STATEMENTS JUST AS A PLACEHOLDER FOR FUTURE CODE.!

for i in range(5):
    pass
print("anything")

n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

n=int(input("enter a number:"))
i=0
sum=0
while i<=n:
    sum+=i
    i+=1
 
    print("sum=",sum)

n=int(input("enter a number:"))
sum=0
i=0
while i<=n:
    i+=1
    sum+=i
print("sum=",sum)

n=int(input("enter a number:"))
fact=1
for i in range(1,n+1):
    fact*=i
    
print("factorial is=",fact)
