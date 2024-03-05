def isPrime(n):
    if n==2:
        return True
    for i in range(2, n+1):
        if(n%i==0):
            return False
        else: 
            return True

