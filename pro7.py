# Use Of Different Operators

bill_id = 1001
customer_id = 101
bill_amount = 199.99

print("bill_id: %d" % bill_id)
print("customer_id: %d" % customer_id)
print("bill_amount: Rs.%f" % bill_amount)

if bill_amount > 500:
    discounted_amount = bill_amount - bill_amount * 2 / 100
else:
    discounted_amount = bill_amount - bill_amount * 1 / 100

print("Discounted Bill Amount: Rs.%f" % discounted_amount)
