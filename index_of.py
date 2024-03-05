def index_of(list, a):
    count =0
    for i in range(0,len(list)):
        if a==list[i]:
            return count
        count+=1
    return -1
    
index_of([42,7,-9,14,8,39,42,8,19,0],2)