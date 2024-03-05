def swap_pairs(list):
    temp=0
    for i in range(0,len(list)-1,2):
        temp=list[i]
        list[i]=list[i+1]
        list[i+1]=temp
    return list
swap_pairs(["a", "bb", "c", "ddd", "ee", "f", "g"])