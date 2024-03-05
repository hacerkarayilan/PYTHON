def num_in_common(l1,l2):
    list=set()
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if l1[i]==l2[j]:
                list.add(l2[j])
    return list
num_in_common( [3, 7, 3, -1, 2, 3, 7, 2, 15, 15] ,[-5, 15, 2, -1, 7, 15, 36])