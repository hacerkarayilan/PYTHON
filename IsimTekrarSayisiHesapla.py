name=input("Enter name: ")
x={}
while name!="":
    if name in x.keys():
        x[name]+=1
    else:
        x[name]=1
    name=input("Enter name: ")
for (k,v) in x.items():
    print("Entry ["+str(k)+"] has count",v)