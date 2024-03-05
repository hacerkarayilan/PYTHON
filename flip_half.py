def flip_half(list):
    temp=0
    count = len(list)
    if count%2==0:
        for i in range(0,len(list)//2):
            if i%2!=0:
                temp=list[i]
                list[i]=list[count-i]
                list[count-i]=temp
        return list
    else:
        for i in range(0,len(list)//2):
                if i%2!=0:
                    temp=list[i]
                    list[i]=list[count-i-1]
                    list[count-i-1]=temp
        return list
flip_half([0, 1, 2, 3, 4, 5, 6])
        

    