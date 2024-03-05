def input_stats(a):
    file=open(a)
    files=file.readlines()
    count=0
    arr=[]
    for i in files:
        part=i.split()
        d=0
        for i in range(0,len(part)):
            d+=len(part[i])
        if d!=0:
            d+=len(part)-1
        arr.append(d)
        count+=1
    toplam=0
    for i in range(0,len(arr)):
        print("Line",i+1,"has",arr[i],"chars")
        toplam+=arr[i]
    bolum=0.0
    bolum=toplam/count
    print(count,"lines; longest =",str(max(arr))+", average =",bolum)
