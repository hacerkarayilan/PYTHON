def starters(list,num):
    dic={}
    a=set()
    for i in list:
        if i!="" and not i[0].lower() in dic.keys():
            dic[i[0].lower()]=1
        elif i!="" and i[0].lower() in dic.keys():
            dic[i[0].lower()]+=1
    for (k,v) in dic.items():
        if v==num or v>num:
            a.add(k)
    return a
starters(['hi', 'how', 'are', 'He', '', 'Marty!', 'this', 'morning?', 'fine.', '?foo!', '', 'HOW', 'A'], 2)
      
        