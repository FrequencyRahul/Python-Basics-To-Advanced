#Error Handling in Python


a=input("Enter a number:")
print(f"Table of {a} :")

print()

try:
    for i in range(0,11):
        print(f"{int(a)} X{i} =",a*i)
except Exception as e:
    print(e)

print()

try:
    for i in range(0,11):
        print(f"{int(a)} X{i} =",a*i)
except Exception as e:
    print("Invalid Input")

print()

try:
    for i in range(0,11):
        print(f"{int(a)} X{i} =",a*i)
except:
    print("Invalid Input")

print()
print("Some important line of code")
print("end")

#Multiple except

print()
print()

try:
    num=int(input("Enter an integer: "))
    a=[6,3]
    a[num]
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Out of index")

