def switch_pairs(a):
    temp=""
    count=len(a)
    for i in range(0,len(a)-1,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    return a
switch_pairs(["a","b","c","d","e"])
    