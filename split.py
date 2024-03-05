def split(list):
    list1=[]
    for i in range(0,len(list)):
        x=list[i]
        if x%2==0:
            list1.append(int(x/2))
            list1.append(int(x/2))
        else:
            list1.append(int(x//2+1))
            list1.append(int(x//2))
    return list1
split([18, 7, 4, 24, 11])