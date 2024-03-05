def print_triangle():
    for i in range(1,5):
        for j in range(1,i+1):
            print("v",end="")
        print()
        for k in range(1,i+1):   
            print("v",end="")
        print()
    print("vvvvv")
    for i in range(1,5):
        for j in range(i,5):
            print("v",end="")
        print()
        for k in range(i,5):   
            print("v",end="")
        print()
        
print_triangle()