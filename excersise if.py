# Price of a house is $1M
# If Buyer has good credit they need to put down 10%
# otherwise they need to put down 20%
# print the down payment

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")
