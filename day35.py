# For loop with else in Python

for i in range(0,5):
    print(i)
else:
    print("Sorry no i")

for i in []:
    print(i)
else: 
    print("sorry no i")

# we can use else with for and while loop which is executed once the loop is completed (it should not be broken due to some condition)

for i in range(0,5):
    print(i)
    if(i==3):
        break
else:
    print("Sorry no i")