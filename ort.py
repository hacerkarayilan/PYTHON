def ort():
    n=int(input("kac sayının ort hesaplamak istersiniz "))
    sum = 0
    for i in range(0,n):
        x=int(input("bir sayı girin "))
        sum+=x
    avg=int((sum/n)*10)/10
    print("ortalama" , avg)
ort()