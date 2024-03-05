def bestAccept():
    index=0
    best_nei=0
    done = False
    arr=[12,22,13,24,5]
    current=arr[index]
    while done == False :
        best_nei = current
        nei_arr=[]
        if index==0:
            nei_arr.append(arr[index+1])
        elif index==len(arr)-1:
            nei_arr.append(arr[index-1])
        else:
            nei_arr.append(arr[index-1])
            nei_arr.append(arr[index+1])
        for i in nei_arr:
            if i > best_nei:
                best_nei = i
        if current == best_nei:
            done=True
        else:
            current=best_nei
            index=arr.index(best_nei)
        print(nei_arr)
    print(best_nei)

bestAccept()