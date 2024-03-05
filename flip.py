file=open("flip.txt").readlines()
x=[]
temp=0
for i in file:
    x.append(i[0:len(i)-1])
for i in range(0,len(x)-1,2):
    temp=x[i].lower()
    x[i]=x[i+1].upper()
    x[i+1]=temp
if len(x)%2!=0:
    x[len(x)-1]=x[len(x)-1].upper()
