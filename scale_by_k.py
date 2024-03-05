#???*
def scale_by_k(list1):
    list2=[]
    for i in range(0,len(list1)):
        x=list1[i]
        if x>0:
            for j in range(x):
                list2.append(x)
    list1=list2        
    print(list1)
scale_by_k([2,-4,5,1,0,3])