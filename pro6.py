# Checking Identity Of Object and type of object

int_a = 10
raw_input = input("Enter Number")
print("Type of int_a: ", type(int_a))
print("Type of raw_input: ", type(raw_input))

if id(int_a) == id(raw_input):
    print("Same Identity")
else:
    print("Different Identity")

# Here Error Will Be Thrown
print(int_a + raw_input)
