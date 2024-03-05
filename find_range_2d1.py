def find_range_2d(list):
    max=0
    min=0
    count=len(list)
    list.sort()
    max=list[count-1]
    min=list[0]
    return max - min +1
find_range_2d([17,7,9,8,6])