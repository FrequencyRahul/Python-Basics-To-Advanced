#String Methods in Python

#Strings are immutable
a="!! Harry !! Harry !!"

print(a.upper())

print(a.lower())

print(a.rstrip("!")) #removes trailing "character"

print(a.replace("Harry","Rahul"))

print(a.split()) 

print(a.split(" "))

blogheading="introduction tO Python"
print(blogheading.capitalize())     #turns first character to uppercase and all other to lowercase

str1="Welcome to the console !!!"
print(str1.center(50))              #center method aligns the string to the center as per the parameters given by user
print(len(str1))                    #it will make length=parameter given by adding space at starting
print(len(str1.center(50)))

str2="Hello Rahul where are you going. Rahul is good boy"
print(str2.count("Rahul"))          #counts no. of times given parameter is present

str3=a
print(str3.endswith("!!"))          #return True if string ends with given parameter
print(str3.endswith("!!",2,4))

str3=a
print(str3.startswith("!!"))          #return True if string start with given parameter
print(str3.startswith("!!",2,4))

str4="He's Dan and He is going to market. He is shopkeeper"
print(str4.find("wow"))
print(str4.find("is"))              #gives the index of first occurance of parameter or -1 if not present.

print(str4.index("is"))             #same as find but returns error if not found.
#str4.index("wow")

print(a.isalnum())                  #returns True if string contains only alphabets and numbers

print(a.isalpha())                  #returns True if string contains only alphabets

print(a.islower())                  #returns True if all character are in lower case

print(a.isupper())                  #return True if all characters are in upper case   

print(a.isprintable())              #returns True if it contains all printable characters (\n,etc is non printable)

print(a.isspace())                  #returns True if it contains spaces.

print(a.istitle())                  #return True if all first letter of each word is capital

print(a.swapcase())                 #uppercase to lowercase and vice versa

print(str4.title())                  #uppercase all first letter of all words in string

print()
print("Even after all these operation our sting a is same:")
print(a) 