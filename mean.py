def mean(average):
    total=0
    count=0
    for i in range(0,len(average)):
        total+=average[i]
        count+=1
    if total==0:
        return 0.0
    return total/count
mean([0.0, 0.0])