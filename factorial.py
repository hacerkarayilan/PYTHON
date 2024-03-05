def factorial(n):
    x=n
    if x==1:
        return 1
    elif x==0:
        return 1
    else:
        for i in range(2, x + 1):
            x=x*(i-1)
        return print(n, "factorial = ",x)
        
    
factorial(5)