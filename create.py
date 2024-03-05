def create(w,h):
    matrix=[[0]*w]*h
    for i in range(h):
        for j in range(w):
            matrix[i][j]=j
    return matrix
create(5,2)