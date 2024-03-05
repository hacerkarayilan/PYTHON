def count (num):
    c=2
    print("1" ,end =",")
    for i in range(2,num):
        if num%i==0:
            c+=1
            print(i ,end =",")
    print(num)
    return c
count(24)