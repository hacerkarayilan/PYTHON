def find_range_2d(list):
    min=100
    max=0
    for i in range(0,len(list)):
        for j in range(0,len(list[i])):
            if list[i][j]<min:
                min=list[i][j]
            if list[i][j]>max:
                max=list[i][j]
    if len(list)==0:
        return []
    return max-min+1
find_range_2d([[8, 3], [5, 7], [2, 4]])