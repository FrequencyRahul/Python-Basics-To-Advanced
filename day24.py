#Tuples in Python
#split: convert string into list of words.
#list: convert string into list of alphabets.
#option + shift + up/down arrow : copy the line paste it in next line in direction of arrow

tup=(1)
print(tup,type(tup))

tup=(1,)
print(tup,type(tup))


a=list(("a",'b","c'))
b=tuple(("a",'b","c'))
print(a,b)
print(type(a),type(b))

#changing tuple values
print()

a=("happy","birthday","abhay")
b=list(a)
print(b,type(b))
b[2]="Ashutosh"
a=tuple(b)
print(a,type(a))

#similarly you can update your tuple by converting it to list and than you can use all funtions of list.

print()


#unpacking a tuple
# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

print()

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)