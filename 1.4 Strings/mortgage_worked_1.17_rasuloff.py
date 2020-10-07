# Exercise 1.10: Making a table
# Modify the program to print out a table showing the month, total paid so far, and the remaining principal. The output should look something like this:

# 1 2684.11 499399.22
# 2 5368.22 498795.94
# 3 8052.33 498190.15
# 4 10736.44 497581.83
# 5 13420.55 496970.98
# ...
# 308 874705.88 3478.83
# 309 877389.99 809.21
# 310 880074.1 -1871.53
# Total paid 880074.1
# Months 310

# Exercise 1.17: f-strings

# Sometimes you want to create a string and embed the values of variables into it.

# To do that, use an f-string. For example:

# >>> name = 'IBM'
# >>> shares = 100
# >>> price = 91.1
# >>> f'{shares} shares of {name} at ${price:0.2f}'
# '100 shares of IBM at $91.10'
# >>>
# Modify the mortgage.py program from Exercise 1.10 to create its output using f-strings. Try to make it so that output is nicely aligned.

# Worked 1.17

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
    
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(f'{month} {round(total_paid, 2)} {round(principal, 2)}')
    # print(month, round(total_paid, 2), round(principal, 2))

print(f'Total paid is {round(total_paid, 2)}')
print(f'In {month} months')

# print('Total paid', round(total_paid, 2))
# print('Months', month)
