def collapse_pairs(n):
    list=n
    if len(list)%2==1:
        for i in range(0,len(list)-1,2):
            list[i+1]=list[i]+list[i+1]
            if list[i+1]%2!=0:
                list[i]=0
            else:
                list[i]=list[i+1]
                list[i+1]=0 
        print(list)
    else:
        for i in range(0,len(list)-1,2):
            list[i+1]=list[i]+list[i+1]
            if list[i+1]%2!=0:
                list[i]=0
            else:
                list[i]=list[i+1]
                list[i+1]=0 
        print(list)
collapse_pairs([7, 2, 8, 9, 4, 22, 7, 1, 9, 10])