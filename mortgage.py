# mortgage.py

def intdec_format(x, i, d):   # float, integer places, decimal palces
    if x == 0:
        a = '0.' + '0' * d
    else:
        x2 = round(x, d)
        a = str(x2)
    l = a.split('.')

    b = " " * (i - len(l[0]))  + l[0]
    l[1].replace(' ', '0')
    if len(l[1]) < d:
        z = '0' * (d - len(l[1]))
        c =  l[1] + z
        return b + '.' + c

    return b + '.' + l[1]


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
while principal > 0:
    month += 1
    if month <= extra_payment_end_month and month >= extra_payment_start_month:
        this_payment = payment + extra_payment
    else:
        this_payment = payment

    principal = principal * (1+rate/12) - this_payment
    if principal < 0:
        principal = 0
    total_paid = total_paid + this_payment
    a = intdec_format( total_paid, 7, 2)
#    b = str(principal)
    b = intdec_format( principal, 7, 5)
    print(f'{month:3.0f}, {a}, {b}')

a = intdec_format( total_paid, 7, 2)
print('Total paid', a, ' over ', month, ' months')
