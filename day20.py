#Functions in Python
#it is a block of code that performs a specific task whenever its called.

# a=int(input())
# b=int(input())
# gmean=(a+b)/2


def calgmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

calgmean(4,6)

def comp(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(a==b):
        print(a,"is equal to",b)
    else:
        print(a,"is less than",b)

comp(3,4)