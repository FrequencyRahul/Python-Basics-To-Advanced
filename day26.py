#Exercise 2 Solution

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