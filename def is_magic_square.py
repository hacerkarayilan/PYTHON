def is_magic_square(list):
    count=0
    list1=[]
    for i in range(0,len(list)):
        count=0
        if len(list)!=len(list[i]):
            return False
        for j in range(0,len(list[i])):
            count+=list[i][j]
        list1.append(count)
    for i in range(0,len(list1)-1):
        if list1[i]!=list1[i+1]:
            return False
    return True
is_magic_square([[2, 7, 6], [9, 5, 1], [4, 3, 8]])