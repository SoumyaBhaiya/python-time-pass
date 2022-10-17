#Made a list
names = ["Harry", "Ron", "Hermoine", "Ginny"]

print(names)
print(names[0])
print("-_-_-________________________________")
names.append("Draco")
#append adds a value in lists
print(names)
print("---------------------------------")
names.sort()
print(names)


#Create an empty set

s = set()

#Add some elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
print(s)
#Notice that 3 did't appeared twice. 
# every element will not repeat itself
print("----------------")
s.remove(2)
print(s)

#len will give you length of a sequence or number of characters or so

print(f"The set has {len(s)} elements")
