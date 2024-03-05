file=open("plus.txt").readlines()
x=[]
artı=0
eksi=0
for i in file:
    x.append(i[0:len(i)-1])
for i in range(1,len(x),2):
    y=x[i]
    artı=0
    eksi=0
    for j in range(0,len(y)):
        if y[j]=="+":
            artı+=1
        else:
            eksi+=1
    sonuc=(artı*100)/(artı+eksi)
    print(str(x[i-1])+": "+str(sonuc)+"%","plus")
