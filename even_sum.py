def even_sum():
    n=int(input("how many integers? "))
    max=0
    sum=0
    for i in range(0,n):
        x=int(input("next integer? "))
        if x%2==0:
            sum+=x
            if x>max:
                max=x
    print("even sum =",sum)
    print("even max =",max)