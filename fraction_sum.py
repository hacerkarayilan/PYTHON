def fraction_sum(n):
    for i in range(1,n+1):
        n+=(1/i)-1
    return n
fraction_sum(3)
    