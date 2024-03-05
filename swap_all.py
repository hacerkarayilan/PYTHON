def swap():
    a1 = [1, 2, 3]
    a2 = [4, 5, 6]
    swap_all(a1, a2)
def swap_all(a1, a2):
    for i in range(0, len(a1)):
        temp = a1[i]
        a1[i] = a2[i]
        a2[i] = temp
    print(a1)
    print(a2)
       
swap() 
