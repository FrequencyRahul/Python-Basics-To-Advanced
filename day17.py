#for loop in Python

colors=['red','blue','green']
for color in colors:
    print(color)
    for i in color:
        print(i, end=',')
    print()
    
for i in range(0,20,2):
    print(i)