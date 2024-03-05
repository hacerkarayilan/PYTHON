def triangle(n):
    for i in range(1,n+1):
        for k in range(i,n):
            print(" ",end="")
        for j in range(0,i):
            print("*",end="")
        print()
triangle(4)