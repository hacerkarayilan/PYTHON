a = [1, 7, 5, 6, 4, 14, 11]
for i in range(0, len(a)-1):
    if (a[i]>a[i+1]):
        a[i+1]=a[i+1]*2
    
    print(a[i], end=" ")
print(a[i+1])