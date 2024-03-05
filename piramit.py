def ti(n):
    for i in range(1,n+1):
        print(" "*(n+1-i),end=" " )
        print("*"*i,end="")
        print()
ti(5)