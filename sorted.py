def sorted(list1):
    count=len(list1)
    list2=[0]*count
    list2=list1
    list1=list1.sort()
    if list1==list2:
        return True
    return False
sorted([1.5, 4.3, 7.0, 19.5, 25.1, 46.2])