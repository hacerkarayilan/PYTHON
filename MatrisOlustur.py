def deneme1(w,h):
    matrix=[]
    for i in range(h):
        row=[0]*w
        for j in range(w):
            row[j]=j
        matrix.append(row)
    return matrix
deneme1(3,4)