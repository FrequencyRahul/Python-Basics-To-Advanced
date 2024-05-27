#Dictionaries in Python

# Ordered collection of data
# They store multiple item in single variable
# Dictionary items are key value pairs seperated by commas and enclosed by {}

dic={
    "Rahul":"IIT Delhi",
    "Ashutosh":"NIT Rourkela",
    "Abhay":"NIT Calicut"
}

print(dic)
print(dic["Rahul"])         #if key do not exist it will throw error   
print(dic.get("Rahul"))     #if key do not exist it will not throw error and print None

print()

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic.get(key)} ")

print()

print(dic.items())      #it gives pair of items in dictionary

print()

for key,value in dic.items():
    print(f"The value corresponding to key {key} is {value}")