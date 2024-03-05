from random import*
def roll_two_dice():
    dgr=int(input("Desired sum: "))
    x=randint(1,6)
    y=randint(1,6)
    print(x,"and",y,"=",(x+y))
    while (x+y)!=dgr:
        x=randint(1,6)
        y=randint(1,6)
        print(x,"and",y,"=",(x+y))
roll_two_dice()