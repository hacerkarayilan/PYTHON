def remove_even_length(list):
    a=[]
    for i in range(0,len(list)):
        if len(list[i])%2==0:
            a.append(list[i])
    for i in range(0,len(a)):
        list.remove(a[i])
    return list
remove_even_length(["This", "is", "a", "test"])     