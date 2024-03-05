def print_number_square(a,b):
    for i in range(a, b+1):
        for j in range(i, b+1):
            print(j, end="")
        for k in range(a,i):
            print(k, end="")
        print()
        
print_number_square(4,7)