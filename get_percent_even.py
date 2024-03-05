def get_percent_even(a):
    count=0
    count1=0
    for i in range(0,len(a)):
        if a[i]%2==0:
            count+=1
        count1+=1
    if count1==0:
        return 0.0
    else:
        y=count*100/count1
        return y