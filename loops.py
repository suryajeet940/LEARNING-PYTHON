#LOOPS ARE USED TO REPEAT A BLOCK OF INSTRUCTIONS.

# COUNT=1
# while COUNT<=5:
#     print("HELLO WORLD!",COUNT)
#     COUNT+=1

# i=1
# while i<=5:
#     print(i)
#     i+=1


# i=1
# while i<=10:
#     print(3*i)
#     i+=1


# n=input("enter a number:")
# i=1
# while i<=10:
#     print(n,"*",i,"=",int(n)*i)
#     i+=1


# n=int(input("enter a number:"))
# i=1
# while i<=10:
#     print(n,"*",i,"=",n*i)
#     i+=1

# nums=[1,2,3,4,5,6,7,8,9]
# idx=0
# while idx<=len(nums)-1:
#     print(nums,idx)
#     idx+=1

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