# Use Of Different Operators

bill_id = 1001
customer_id = 101
bill_amount = 1200.00
discount = 0

print("bill_id: %d"%bill_id)
print("customer_id: %d"%customer_id)
print("bill_amount: Rs.%f"%bill_amount)

if bill_amount >= 1000 :
    discount = 5
elif bill_amount >=500  and bill_amount <1000:
    discount = 2
elif bill_amount>0 and bill_amount<500:
    discount = 1

discounted_amount = bill_amount - bill_amount * discount/ 100
print("Discounted Bill Amount: Rs.%f" %discounted_amount)