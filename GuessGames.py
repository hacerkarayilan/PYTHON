from random import *
def gu():
    print("This program allows you to guess random numbers.")
    print("I will think of a number between 1 and 100")
    print("and you will try to guess it.")
    print("After each guess, I will give you a clue about")
    print("whether the correct number is higher or lower.")
    print()
def guess():
    count=1
    print("I'm thinking of a number between 1 and 100...")
    x=randint(1,100)
    guess=0
    while guess!=x:
        guess=int(input("Your guess? "))
        if guess>x:
            print("It's lower.")
        elif guess<x:
            print("It's higher.")
        else:
            print("You got it right in",count,"guesses!")
        count+=1
def ret():
    gu()
    guess()
    count1=0
    play=input("Do you want to play again? ")
    while play!="no" or play!="No" or play!="Okay" or play!="0" or play!="certainly" or play!="hello":
        if play=="y" or play=="yes" or play=="Y" or play=="YES" or play=="Yes" or play=="yeehaw":
            guess()
            count1+=1 
        play=input("Do you want to play again? ")
    sonuc()
            
def sonuc():
    print("Overall results:")
    print("Total games   =",count1)
                
ret()
