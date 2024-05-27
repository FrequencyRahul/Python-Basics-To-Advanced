#Finally keyword in Python

#confusion and hard stuff starts from today


try:
    print(x)

except NameError:
    print("variable is not defined")
# except Exception as e:
#     print("error")
# except:
#     print("something else went wrong")
finally:
    print("I handled the error")


#The try block will raise an error when trying to write to a read-only file:
print()
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    print('finally')
except:
  print("Something went wrong when opening the file")  


print()
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")