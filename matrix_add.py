def matrix_add(l1,l2):
    a=[]
    for i in range(0,len(l1)):
        count=[]
        for j in range(0,len(l1[i])):
            count.append(l1[i][j]+l2[i][j])
        a.append(count)
    return a
matrix_add([[1, 2, 3], [4, 4, 4]], [[5, 5, 6], [0, -1, 2]])