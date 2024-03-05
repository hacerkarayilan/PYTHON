def n_copies(list):
    count=len(list)
    count1=0
    count2=0
    for i in range(0,len(list)):
        x=list[i]
        if x>0:
            count1+=x
    list1=[0]*count1
    for j in range(0,len(list)):
        y=list[j]
        if y>0:
            for k in range(count2,count2+y):
                list1[k]=list[j]
        
            count2+=y
    return list1
n_copies([3,5,0,2,2,-7,0,4])