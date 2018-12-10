# List Data structure Demo
#Remove Duplicate

names = ["ramu", "shyamu", "kanu", "manu", "ramu","radha", "manu"]

t = []

print("Before Duplicate: ")
print(names)

for x in names:
    if x not in t:
        t.append(x)

print("Duplicate Remvoed: ")
print(t)