# interest.py

principal = 1000
rate = 0.05
numyears = 5
year = 1

while year < numyears:
    principal = principal * ( 1  + rate)
    # See Ch. 9 for format string details
    # >3d is 3 decimals right aligned
    # <3d is 3 decimals left aligned
    print(f'{year:<2d} {principal:0.2f}')
    # this is more verbose but does the similar thing
    # d = '{year} {principal}'.format(year=year, principal=principal)
    # print(d)
    year += 1

