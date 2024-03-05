def find_median(a):
    list = a
    temp=0
    for i in range(0,len(list)):
        for j in range(i,len(list)):
            if list[i]>list[j]:
                temp=list[i]
                list[i]=list[j]
                list[j]=temp
    x=len(list)//2
    print(list[x])
find_median([5, 2, 4, 17, 55, 4, 3, 26, 18, 2, 17])
        