#Dictionary Methods in Python

ep1={1:45,2:70,3:54,4:80}
ep2={5:43,6:98}

print(ep1,ep2)
ep1.update(ep2)
print(ep1)

#ep1.clear() : it will empty dict ep1
#ep1.pop(key): it will remove key value pair according to key passed
#ep1.popitem() : it will remove last key-value pair
#del ep1 : it will delete the dict ep1
#del ep1[key] : it will remove key-value pair according to key passed
#ep1.update(key:value) : update value of key if its already present otherwise it creates new key value pair.

ep1.update({1:26})
ep1.update({10:66})
print(ep1)