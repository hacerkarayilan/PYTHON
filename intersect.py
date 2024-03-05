def intersect(l1,l2):
    dic={}
    for (k,v) in l1.items():
        for (a,b) in l2.items():
            if a==k and b==v:
                dic[a]=b
    return dic

intersect({'Janet': 87, 'Logan': 62, 'Whitaker': 46, 'Alyssa': 100, 'Stefanie': 80, 'Jeff': 88, 'Kim': 52, 'Sylvia': 95},
{'Logan': 62, 'Kim': 52, 'Whitaker': 52, 'Jeff': 88, 'Stefanie': 80, 'Brian': 60, 'Lisa': 83, 'Sylvia': 87})