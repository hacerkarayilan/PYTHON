def boy_girl():
    file=open("boyGirl.txt").read().split()
    arr=[]
    arr=file
    isim=[]
    sayi=[]
    kiz=0
    erkek=0
    ksum=0
    esum=0
    for i in range(0,len(arr)):
        if i%2==0:
            isim.append(arr[i])
        elif i%2!=0:
            sayi.append(arr[i])
    for i in range(0,len(isim)):
        if i%2==0:
            erkek+=1
            esum=esum+int(sayi[i])
        elif i%2!=0:
            kiz+=1
            ksum=ksum+int(sayi[i])
    print(erkek,"boys",kiz,"girls")
    print("Difference between boys' and girls' sums:",(ksum-esum))