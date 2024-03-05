def num(n):
    x=[0]*10
    while n>0:
        n1=n%10
        n=n//10
        x[n1]+=1
    m=x[0]
    p=0
    for i in range(1, len(x)):
        if x[i]>m:
            m=x[i]
            p=i
    return p,x
num(31212234)
    