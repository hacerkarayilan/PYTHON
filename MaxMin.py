x=int(input("How many numbers? "))
max1=-1000
min1=1000
for i in range(0,x):
    a=int(input("Next numbers? "))
    if a<min1:
        min1=a
    if a>max1:
        max1=a
print("Biggest =",max1)
print("Smallest =",min1)

    