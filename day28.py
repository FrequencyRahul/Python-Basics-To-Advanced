# f-string in Python


#previors method : can be used be little complicated.
letter= "my name is {} and I am from {}"
country= "India"
name="Rahul"

print(letter.format(name,country))
print(letter.format(country,name))

letter= "my name is {1} and I am from {0}"
print(letter.format(country,name))


print()
#new method 

print(f"my name is {name} and I am from {country}")


print()
txt="for only {price: .2f} dollars!"
print(txt.format(price=49.09999))

print()
price=49.0999
txt= f"for only {price:.2f} dollars"
print(txt)

print()
print(f"{(2*4)+34}")

print(f"here i leaned about f-strings {{name}} will be replaced be {name} ")