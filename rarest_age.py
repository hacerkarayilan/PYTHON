def rarest_age(age):
    dic={}
    min=10000
    yas=10000
    for (k,v) in age.items():
        if v in dic:
            dic[v]+=1
        else:
            dic[v]=1
    for (k,v) in dic.items():
        if v<min:
            min=v
            yas=k
        elif v==min:
            if k<yas:
                yas=k
    return yas
rarest_age({'Char': 45, 'Dan': 45, 'Jerry': 23, 'Kasey': 10, 'Jeff': 10, 'Elmer': 45, 'Kim': 10, 'Ryan': 45, 'Mehran': 23})