def num(n):
    x=[0]*10
    while n>0:
        n1=n%10
        n=n//10
        x[n1]+=1
    #return x
    return x.index(max(x))
num(12312512122)