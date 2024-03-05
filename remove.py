def remove(list):
    count = 0
    while count<len(list)-1:
        if list[count]==list[count+1]:
            list.pop(count)
        else:
            count+=1
    return list
remove([-2, 1, 1, 3, 3, 3, 4, 5, 6, 78, 78, 79])