#Match Case Statements in Python

x=int(input("Enter the value of x"))
match x:
    case 0:
        print("x is 0")
    case 4:
        print("x is 4")
    case _ if x!=80:     #default case 
        print(x,"x is not 80")

    case _ if x!=90:     #default case 
        print(x,"x is not 90")
    case _ :     #default case 
        print(x)