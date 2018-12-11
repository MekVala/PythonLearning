# Dictionay Demo

car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
}

print("Values:")
for v in car1.values():
    print(v)

print("Keys:")
for v in car1.keys():
    print(v)


# Mutable
car1["automatic"]= False
print("\n",car1["automatic"])