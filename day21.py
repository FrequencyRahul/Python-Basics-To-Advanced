#Function Argument in Python
""" There are four types of arguments in Python
    1) Default Argument : funtion assumes a default value even if a value is not provided
    2) Keyword Argument
    3) Variable Length Argument
    4) Required Argument
    """
    
def avg(a=9,b=1): #default arguments
    print("The avergae is:",(a+b)/2)

avg()
avg(b=10)
avg(5)


print()


def name(fname,mname="john",lname="watson"): #fname is required argument
    print("Hello",fname,mname,lname)

name("Rahul","Singh","Rawat")
name("Smith")
name("Rober","Downy")



print()


def average(*numbers): #*numbers create tuple named numbers
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average:",sum/len(numbers))

average(2,4)
average(2,4,6,8,10)


print()


def name(**name): #**name creates dictionary named name
    print(type(name))
    print("Hello",name['fname'],name["mname"],name["lname"])

name(mname="Bachchan",lname="Singh",fname="Amitabh")
    

print()


#return : It is used to return the value of the value of expression back to the calling function.

def average(*numbers): #*numbers create tuple named numbers
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    return ("Average:",sum/len(numbers))

print(average(2,4))
print(average(2,4,6,8,10))