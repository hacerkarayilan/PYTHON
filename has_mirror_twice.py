def has_mirror_twice(a1,a2):
    count=0
    x=0
    y=0
    for i in range(0,len(a1)):
        for j in range(count,count+1):
            x=a2[count]
        if a2[count]==a1[i]:
            count+=1
            if count==len(a2):
                y+=1
                count=0
        else:
            count=0
        if count==len(a2):
            y+=1
    if y>=2:
        return True
    return False
has_mirror_twice([6, 1, 2, 1, 3, 1, 3, 2, 1, 5],[1,2])