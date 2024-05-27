#String Slicing

name="Rahul, Ashutosh"
print(name[0:5])
size=len(name)
print(name[1:size])
print(name[:])  #defaul[0:size]

#negetive slicing
print(name[1:-4])
print(name[1:size-4])

print(name[-3:-1])