#break and continue 

#break: It terminates the loop it lies within.

for i in range(12):
    if(i==10):
        print("Terminates the iteration")
        break 
    if(i==5):
        print("skips this iteration")
        continue
    print("5 X",i+1,"=",5*(i+1))
    
#creating (do-while loop: this loop work atleast once whether the condition is true or false.) in Python
 