#List

names = ["Alo","Marco","Lucia"]
print(len(names))
print(names)

names.append("Eustaquio")
print(names)

print(names[1])
print(names[0:3])

print("------------------Loop 01--------------------------")

for name in names:
    print(name)

print("------------------Loop 02--------------------------")

for index in range(0,len(names)):
    print(names[index])