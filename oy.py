file=open(oy.txt").read().split()
x=[]
y=[]
max=0
isim=""
max1=0
isim1=""
for i in range(0,len(file)):
    if file[i]=="s":
        x.append(file[i-1])
        x.append(int(file[i+1]))
    elif file[i]=="j":
        y.append(file[i-1])
        y.append(int(file[i+1]))
for i in range(1,len(y),2):
    if y[i]>max:
        max=y[i]
        isim=y[i-1]
for i in range(1,len(x),2):
    if x[i]>max1:
        max1=x[i]
        isim1=x[i-1]
print("Sophomore Class President:",isim,"("+str(max)+" votes)")
print("Junior Class President:",isim1,"("+str(max1)+" votes)")