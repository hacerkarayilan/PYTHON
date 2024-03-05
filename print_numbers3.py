def print_numbers3():
    for i in range(1,6):
        for a in range(i,5):
            print(".",end="")
        print(i, end="")
        for l in range(1,i):
            print(".",end="")
        print()
        
print_numbers3()

           