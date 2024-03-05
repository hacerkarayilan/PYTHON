def longest_sorted_sequence(list):
    count=0
    max=0
    count1=len(list)
    for i in range(0,len(list)-1):
        if list[i]<=list[i+1]:
            max+=1
        else:
            max=0
        if max>0 and max>count:
            count=max
    if count1==0:
        return 0
    return count+1
longest_sorted_sequence([17, 42, 3, 5, 5, 5, 8, 2, 4, 6, 1, 19])
    