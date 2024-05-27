#Typecasting in Python
a1=1
b1=2

a2="1"
b2="2"

print(a1+b1)

print(a2+b2)
print(int(a2)+int(b2))

#Types of Typecasting:
#1)Explicit: Coversion done manually 
# ex- int(), float(), hex(), oct(), str(), etc
#2)Implicit: Python convets lower data type to higher data type to prevent data loss

x=2
y=3.4
print(x+y)  #it will print 5.4 which is float a higher data type 