def count_factors(n):
    count=0
    if n==1:
        return 1
    else:
        for i in range(1,n+1):
            if n%i==0:
                count+=1
        return count
count_factors(12)