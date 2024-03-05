def prime_factors(a):
    if a>=2:
        print("2",end="")
        for i in range(3,a+1):
            if count_factors(i)==2:
                print("," + str(i), end="")
                
prime_factors(11)
