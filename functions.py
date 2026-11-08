#BLOCK OF CODE THAT  PERFORMS A SPECIFIC TASK.!!

def function_sum(a,b):
    sum=a+b
    print(sum)
    return sum
function_sum(5,56)
function_sum(34,45)

def calc_fact(n):
    fact=1
    # n=int(input("enter a no.:"))
    for i in range(1,n+1):
        fact=fact*i
    print("fact=",fact)


calc_fact(5)
calc_fact(6)

def calc_product(a,b):
    print(a*b)
    return a*b
calc_product(5,9)

def print_len(list):
    print(len(list))
heroes=["spiderman","superman"]
print_len(heroes)


def print_list(list):
    for items in list:
        print(items)

print_list(heroes)
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

calc_fact(5)
calc_fact(6)

def converter(usd_val):
    inr_val=usd_val*83
    print(inr_val)
    return inr_val
converter(10)

def num_is(n):
    if(n%2==0):
        print(n,"is even")
    else:print(n,"is odd")
num_is(55)
num_is(66)