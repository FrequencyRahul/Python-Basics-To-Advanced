#List 
# ordered collection of data seperated by commas

l=[2,4,6,8,"Rahul", True]
print(l)
print(type(l))
print(l[0])

if (True in l):
    print("yes")
else:
    print("No")

print(l[1:-1])
print(l[::2])

print()

#list comprehension
lst=[i**2 for i in range(4)]
print(lst)

print()

lst=[i*i for i in range(10) if i%2==0]
print(lst)