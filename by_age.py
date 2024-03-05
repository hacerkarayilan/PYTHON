def by_age(ages,x,y):
    dic={}
    for k,v in ages.items():
        if v > x and v<y:
            if v in dic.keys():
                dic[v]+=k
            elif not(v in dic.keys()):
                dic[v]=k
    return dic
by_age({'Allison': 18, 'Benson': 48, 'David': 20, 'Erik': 20, 'Galen': 15, 'Grace': 25, 'Helene': 40, 'Janette': 18, 'Jessica': 35, 'Marty': 35, 'Paul': 28, 'Sara': 15, 'Stuart': 98, 'Tyler': 6, 'Zack': 20}, 16, 25)