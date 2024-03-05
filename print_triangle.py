def print_triangle():
    for i in range(1,8):
        for a in range(i,8):
            print(end=" ")
        for j in range(1,2*i-2):
            print("*",end="")

        print()
print_triangle()