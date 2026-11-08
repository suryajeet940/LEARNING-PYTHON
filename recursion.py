#WHEN A FUNTION CALL ITSELF REPEATEDLY!!

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(6)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
      result=n*fact(n-1)
      print(result)
      return result
    
fact(5)

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
print(fact(0))

def fib(n):
    if(n==0):
        return 0
    else:
        return n+fib(n-1)

print(fib(5))
print(fib(1))
print(fib(6))

def print_list(list,idx=0):
    if(idx==len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)

cities=["mirzapur","pune","mumbai"]
print_list(cities)