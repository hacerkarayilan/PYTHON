def contains(a1, a2):
    list1=a1
    list2=a2
    count=0
    for i in range(0, len(list1)):
        y=list1[i]
        for j in range(count,count+1):
            x=list2[j]
            if y==x:
                count+=1
                if count==len(list2):
                    return True
            else:
                count=0
    return False
    
contains([1,1, 2, 1,1], [1, 2, 1])