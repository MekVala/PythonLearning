# Swap Two Numbers without using temp

x = 5
y = 20
print("Before Swap : X=",x,"Y=",y)

x = x + y
y = x - y
x = x - y

print("After Swap : X=",x,"Y=",y)