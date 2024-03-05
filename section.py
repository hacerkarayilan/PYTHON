def hesap():
    lines=open("/python/section.txt").readlines()
    sec=1
    for line in lines:
        print("section" ,sec)
        points=[0]*5
        grades=[0]*5
        sec+=2
hesap()