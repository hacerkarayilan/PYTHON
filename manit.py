def manit(n):
    for i in range(0,n):
        for j in range(0,i):
            print("o",end="")
        print("x",end="")
        for a in range(i,n-2):
            print("o", end="")
            
        print()
        
manit(5)