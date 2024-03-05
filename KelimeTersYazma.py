x=input("bir kelime girin  ")
y=""
for i in range(len(x)-1,-1,-1):
    y = y + x[i]
print(y)