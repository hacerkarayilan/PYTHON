def max_length(a):
    max=0
    if len(a)==0:
        return 0
    else:
        for i in a:
            if max<len(i):
                max=len(i)  
        return max
max_length({"a", "bb", "ccc", "d"})