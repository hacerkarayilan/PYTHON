def count_duplicates(a):
    list=a 
    eleman=0   
    list1=[0]*100
    for j  in range(0,len(list)):
        x=list[j]
        list1[x]+=1
    for k in range(0,len(list1)):
        y=list1[k]
        if y>0:
            eleman+=1
    return eleman
            
count_duplicates([0, 0, -1, -1, -1, 5, 5, 5, 0, 0]) 