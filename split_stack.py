def split_stack(list):
    a=[]
    list.reverse()
    a=list
    list=[]
    for i in range(0,len(a)):
        if a[i]<0:
            list.append(a[i])
    for i in range(0,len(a)):
        if a[i]>=0:
            list.append(a[i])
    return list
split_stack([1, -2, 3, -4, 5, -6])