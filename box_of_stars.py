def box_of_stars(a,b):
    for i in range(1,a+1):
        print("*",end="")
    print()
    for x in range(1,b-1):
        print("*" , end="")
        for y in range(1,a-1):
            print(" ", end="")
        print("*")
    for i in range(1,a+1):
        print("*",end="")
        
    
box_of_stars(8,5)    