def binary_to_decimal(x):
    a=0
    kalan=0
    count=0
    while(x>0):
        kalan=x%10
        a+=kalan*2**count
        x=x//10
        count+=1
    return a
binary_to_decimal(1110)
        
        