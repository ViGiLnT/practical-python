# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
payment = 2684.11

while principal > 0:
    if (month >= extra_payment_start_month) and (month <= extra_payment_end_month):
        payment = 2684.11 + 1000
    else:
        payment = 2684.11

    if (principal * (1+rate/12)) < 0:
        principal = principal * (1+rate/12)
        total_paid = total_paid
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    
    month = month + 1

print('Total paid', total_paid, 'in', month, 'months')