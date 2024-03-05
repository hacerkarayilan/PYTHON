n=1
sum=0
count=0
while n!=0:
    n=int(input("Integer? "))
    if n%2==0:
        count+=1
        sum+=n
print("Average:",sum/(count-1))
      