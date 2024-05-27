#Exercise2: Good Morning Sir

"""Problem : Create a python program capable of greeting you. Your program should use time module to the current hour."""

# import time
# a=time.time()       #gives time in seconds from the epoch
# print(a)
# hour=a//(60*60)       #My aproach was wrong
# print(hour)
# seconds1=a%(60*60)
# minutes=seconds1//60
# seconds=minutes%60

# if(12>hour>=0):
#     print("Good Morning")
# elif(4>hour>=12):
#     print("Good Afternoon")
# else:
#     print("Good Evening")



#   or
import time
timestamp=time.strftime('%H: %M: %S')
print(timestamp)
timestamp=int(time.strftime('%H'))
print(timestamp)
# timestamp=int(time.strftime('%M'))
# print(timestamp)
# timestamp=int(time.strftime('%S'))
# print(timestamp)
if (0<=timestamp<12):
    print("Good Morning")
if (16>timestamp>=12):
    print("Good Afternoon")
if (16<=timestamp):
    print("Good Evening")