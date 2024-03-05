files=open("coin.txt")
file=files.read().split()
count=0
for i in file:
    if i.lower()=="h" or i.lower()=="heads":
        count+=1
sonuc=(100*count)/len(file)
if sonuc>=50:
    print(count,"heads","("+str(sonuc)+"%)")
else:
    print("You lose!")