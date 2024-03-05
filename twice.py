def twice(v):
    z=set()
    count = 0
    for i in range(0,len(v)):
        count=0
        for j in range(0,len(v)):
            if v[i]==v[j]:
                count+=1
        if count==2:
            z.add(v[i])
    return z
twice([1, 3, 1, 4, 3, 7, -2, 0, 7, -2, -2, 1])