def deneme(w,h):
    list=[[0]*w]*h
    for i in range(h):
        for j in range(w):
            list[i][j]=j
            print(list[i][j]," ",end="")
        print()
    return list
m=deneme(5,5)
m1[1][1]=5
m1