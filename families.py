dic.pop(x)file=open("families.txt").read().split()
arr=[]
arr=file
dic = {}
for i in range(1,len(arr),2):
    if arr[i] in dic.keys():
        dic[arr[i]]+=1
    else:
        dic[arr[i]]=1
        
x=max(dic.keys())
print(x,"family:",end=" ")
for i in range(0,len(arr)):
    if arr[i]==x:
        print(arr[i-1],end=" ")
print()
