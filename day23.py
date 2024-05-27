#List Methods in Python

# append()	: Adds an element at the end of the list
# clear()	: Removes all the elements from the list
# copy()	: Returns a copy of the list
# count()	: Returns the number of elements with the specified value
# extend()	: Add the elements of a list (or any iterable), to the end of the current list
# index()	: Returns the index of the first element with the specified value
# insert()	: Adds an element at the specified position
# pop()	    : Removes the element at the specified position
# remove()	: Removes the item with the specified value at first occurance
# del()     : Removes the specified index or delete the list completely.
# reverse()	: Reverses the order of the list
# sort()	: Sorts the list
# clear()   : Empties the list. 

"""

del:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

"""


"""

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


Change in list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

"""

l=[1,4,8,2,5,65,33,2,223435,787,90]
l.sort()
print(l)
print()

l.append(5)
print(l)
print()

l.pop(4)
print(l)
print()

del(l[3])
l.remove(787)
print(l)
print()


#imp 
m=l
m[0]=5
print(l)    #l[0] is also change
print()

m=l.copy()
m[0]=8      #l[0] is not affected
print(l)
