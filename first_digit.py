def first_digit(n):
    while abs(n)>=10:
        n=n/10
    return int(abs(n))
first_digit(-947)