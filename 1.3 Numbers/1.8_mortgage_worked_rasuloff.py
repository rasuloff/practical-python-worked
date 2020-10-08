# Exercise 1.8: Extra payments
# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.

# When you run the new program, it should report a total payment of 929,965.62 over 342 months.

# Worked 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment

    if month >= 1 and month <= 12:
        principal = principal - 1000
        total_paid = total_paid + 1000

print('Total paid', total_paid)
print('Month', month)
