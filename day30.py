#Recursion in Python
#function calls itself

#factorial(n)=n*factorial(n-1)
def factorial(n):
    if(n==1):
        return 1
    return n*factorial(n-1)


print(factorial(5))

print()
#fibonacci series
#third=first+second
n=int(input())
def fib(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(n))