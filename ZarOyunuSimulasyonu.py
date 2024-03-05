from random import*
print("Welcome to Piglet!")
x=randint(1,6)
y=0
while(x!=1):
    print("You rolled a ",x)
    y+=x
    x=randint(1,6)
    girdi=input("Roll again? ")
    if x==1:
        print("You rolled a 1")
        print("You got 0 points. ")
        y==0
    if girdi=="no":
        print("You got",y," points.")
        break
