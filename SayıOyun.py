from random import randint
a,b=0,0
count=0
while a+b!=7:
    a=randint(1,6)
    b=randint(1,6)
    print(a,"+",b,"=",(a+b))
    count+=1
print(count, ". denemede buldunuz")