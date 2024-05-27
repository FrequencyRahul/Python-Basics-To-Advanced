#Operations on Tuples


#1) You can convert tuple to list, do all the operation and than convert it back to tuple

tup=(2,4,6,8)
lst=list(tup)
lst1=[19,4,5,3]
lst.append("rahul")
print(lst)
lst.pop(1)
print(lst)
lst.extend(lst1)
print(lst)

tup=tuple(lst)
print(tup)

print()
# 2) Some methods of tuple
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

tup1=(0,5,30,5,3,7,56,3,340)
res=tup1.count(3)
print("count of 3 in tup1 is :",res)
res=tup1.index(3)
res1=tup1.index(3,5,len(tup1))
print("index of first occurance of param. in tup1 :",res)
print("index of occurance of param. in tup1 between index 3 and last index :",res1)
