#Set methods in Python

# Both of these prints all items that are present in two sents: 
#union(): returns new set
#update(): adds items into existing set from another set

s1={8,2,5,6}
s2={9,6,7}
print(s1.union(s2))
print(s1,s2)

print()

s1.update(s2)
print(s1,s2)

print()

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo"}

cities3=cities1.union(cities2)
print(cities3)

print()

# Both of these prints common items that are present in two sents:
# intersection(): returns new set
# intersection_update(): adds items into existing set from another set

cities4=cities2.copy()
cities2.update(cities1)
print(cities2)

print()


print(cities4.intersection(cities1)) # here it created a new set containing intesection items.
cities4.intersection_update(cities1) # here it updated cities4 with intersection itesms.
print(cities4)

print()

#Symmetric Difference : all the values not present in both sets.
#symmenteric_difference() : returns new set
#symmenteric_difference_update() : update a existing set.

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo"}
a=cities1.symmetric_difference(cities2)
print(a)
cities1.symmetric_difference_update(cities2)
print(cities1)

print()

#Difference : all values not present in original set excluding common items between original and other set.
# differecne() : returns new set
# differnce_update(): update a existing set.

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo"}
a=cities1.difference(cities2)
print(a)
cities1.difference_update(cities2)
print(cities1)

print()

#isdisjoint() : return True if the two are disjoint sets(no common element)

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo"}
print(cities1.isdisjoint(cities2))
print()

#issuperset() : return true if s1 has all elements of s2  -> s1.issuperset(s2)

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo"}
print(cities1.issuperset(cities2))
print()

#issubset() : returns True if s2 has all elements of s1  -> s1.issubset(s2)

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities2={"Almora","Delhi","Chamoli","Tokyo","Delhi","Mumbai","Kolkata","Joshimath"}
print(cities1.issubset(cities2))
print()

#both removes the item from the set
#remove() : error if item is not present
#discard() : no error if item is not present

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities1.discard("Delhi")

cities1.discard("Delhi")

print()

cities1={"Delhi","Mumbai","Kolkata","Joshimath"}
cities1.remove("Delhi")
cities1.remove("Delhi")

#pop() : removes any element from the set and removed item may change (It also returns the removed item)
#del set : deletes the set
#set.clear() : removes all values of the set

# you can itereate in set similiar as list, etc.