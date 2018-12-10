# Iterative Control Structure

amount = 100.0
interest = 0.0
months = 1

while months < 6:
    interest = amount * 0.2
    amount = amount + interest
    months += 1

print(amount)